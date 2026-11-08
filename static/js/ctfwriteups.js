
const SEARCH_DEBOUNCE_DELAY = 300;

let searchDebounceTimer;
let writeupsAbortController;

const loadingState = document.getElementById("loading");
const errorState = document.getElementById("error");
const emptyState = document.getElementById("empty");
const gridContainer = document.getElementById("grid");

const searchForm = document.getElementById("writeup-search-form");
const searchInput = document.getElementById("search-input");
const writeupForm = document.getElementById("writeup-form");

function getCSRFToken() {
    const token = document.querySelector(
        '[name="csrfmiddlewaretoken"]'
    );

    return token ? token.value : "";
}

function displayPageSection({
    showLoading = false,
    showError = false,
    showEmpty = false,
    showGrid = false,
}) {
    loadingState.classList.toggle("hide", !showLoading);
    errorState.classList.toggle("hide", !showError);
    emptyState.classList.toggle("hide", !showEmpty);
    gridContainer.classList.toggle("hide", !showGrid);
}

function buildWriteupCardElement(writeup) {
    const article = document.createElement("article");
    article.className = "ctf-card";

    const title = document.createElement("h2");
    title.textContent = writeup.title;

    const content = document.createElement("div");
    content.className = "ctf-content";

    if (writeup.description) {
        const description = document.createElement("p");
        description.textContent = writeup.description;
        content.appendChild(description);
    }

    const actions = document.createElement("div");
    actions.className = "ctf-actions";

    if (writeup.writeup_url) {
        const link = document.createElement("a");

        link.href = writeup.writeup_url;
        link.textContent = "Open";
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.className = "btn-read-pdf";

        actions.appendChild(link);
    }

    // Tombol Star
    const starButton = document.createElement("button");

    starButton.type = "button";
    starButton.className = "button button-star";

    if (writeup.is_starred) {
        starButton.classList.add("is-starred");
    }

    starButton.dataset.action = "star";
    starButton.dataset.id = writeup.id;

    starButton.innerHTML = `
        <span aria-hidden="true">★</span>
        ${writeup.is_starred ? "Unstar" : "Star"}
        <span class="star-count">
            ${Number(writeup.star_count) || 0}
        </span>
    `;

    starButton.title = writeup.starred_by_names
        ? `Diberi star oleh ${writeup.starred_by_names}`
        : "Jadilah yang pertama memberi star";

    actions.appendChild(starButton);

    // Tombol Edit khusus Editor dan Superuser
    if (CAN_EDIT) {
        const editButton = document.createElement("button");

        editButton.type = "button";
        editButton.className = "button button-secondary";
        editButton.textContent = "Edit";
        editButton.dataset.action = "edit";
        editButton.dataset.id = writeup.id;

        actions.appendChild(editButton);
    }

    // Tombol Delete khusus superuser
    if (IS_SUPERUSER) {
        const deleteButton = document.createElement("button");

        deleteButton.type = "button";
        deleteButton.className = "button button-secondary";
        deleteButton.textContent = "Delete";

        deleteButton.dataset.action = "delete";
        deleteButton.dataset.id = writeup.id;

        actions.appendChild(deleteButton);
    }

    content.appendChild(actions);
    article.append(title, content);

    return article;
}

// GET: Mengambil daftar write-up
async function fetchWriteups(searchQuery = "") {
    if (writeupsAbortController) {
        writeupsAbortController.abort();
    }

    writeupsAbortController = new AbortController();

    try {
        displayPageSection({ showLoading: true });
        gridContainer.innerHTML = "";

        const url = searchQuery
            ? `${BASE_WRITEUPS_ENDPOINT}?title=${encodeURIComponent(searchQuery)}`
            : BASE_WRITEUPS_ENDPOINT;

        const response = await fetch(url, {
            headers: {
                "Accept": "application/json",
            },
            signal: writeupsAbortController.signal,
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const writeups = await response.json();

        if (!Array.isArray(writeups)) {
            throw new Error("Format data API tidak sesuai.");
        }

        if (writeups.length === 0) {
            displayPageSection({ showEmpty: true });
            return;
        }

        writeups.forEach(writeup => {
            gridContainer.appendChild(
                buildWriteupCardElement(writeup)
            );
        });

        displayPageSection({ showGrid: true });

    } catch (error) {
        if (error.name === "AbortError") {
            return;
        }

        console.error("Error loading write-ups:", error);
        displayPageSection({ showError: true });
    }
}

// POST: Toggle star
async function toggleStar(writeupId) {
    const url = TOGGLE_STAR_URL.replace(
        "00000000-0000-0000-0000-000000000000",
        encodeURIComponent(writeupId)
    );

    try {
        const response = await fetch(url, {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "Accept": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        await fetchWriteups(searchInput.value.trim());

    } catch (error) {
        console.error("Error updating star:", error);

        showToast(
            "Gagal",
            "Tidak dapat memperbarui star. Pastikan kamu sudah login.",
            "error"
        );
    }
}

// DELETE: Menghapus write-up
async function deleteWriteup(writeupId) {
    if (!confirm("Yakin ingin menghapus write-up ini?")) {
        return;
    }

    const url = DELETE_WRITEUP_URL.replace(
        "00000000-0000-0000-0000-000000000000",
        encodeURIComponent(writeupId)
    );

    try {
        const response = await fetch(url, {
            method: "DELETE",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Accept": "application/json",
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        showToast(
            "Berhasil",
            "Write-up berhasil dihapus!",
            "success"
        );

        await fetchWriteups(searchInput.value.trim());

    } catch (error) {
        console.error("Error deleting write-up:", error);

        showToast(
            "Gagal",
            "Tidak dapat menghapus write-up.",
            "error"
        );
    }
}

// Event listener untuk tombol Star, Edit, dan Delete
gridContainer.addEventListener("click", event => {
    const button = event.target.closest("button[data-action]");

    if (!button) return;

    const writeupId = button.dataset.id;

    if (button.dataset.action === "star") {
        toggleStar(writeupId);
    }

    if (button.dataset.action === "edit") {
        openEditModal(writeupId);
    }

    if (button.dataset.action === "delete") {
        deleteWriteup(writeupId);
    }
});

// Pencarian write-up dengan debounce
function searchWriteups() {
    fetchWriteups(searchInput.value.trim());
}

searchInput.addEventListener("input", () => {
    clearTimeout(searchDebounceTimer);

    searchDebounceTimer = setTimeout(() => {
        searchWriteups();
    }, SEARCH_DEBOUNCE_DELAY);
});

searchForm.addEventListener("submit", event => {
    event.preventDefault();

    clearTimeout(searchDebounceTimer);
    searchWriteups();
});

// POST: Menambahkan write-up
if (writeupForm) {
    writeupForm.addEventListener("submit", async event => {
        event.preventDefault();

        const submitButton = writeupForm.querySelector(
            'button[type="submit"]'
        );

        submitButton.disabled = true;

        try {
            const formData = new FormData(writeupForm);
            const data = {};

            for (const [key, value] of formData.entries()) {
                if (key !== "csrfmiddlewaretoken") {
                    data[key] = value;
                }
            }

            const response = await fetch(CREATE_WRITEUP_ENDPOINT, {
                method: "POST",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify(data),
            });

            const result = await response.json().catch(() => ({}));

            if (!response.ok) {
                throw new Error(
                    JSON.stringify(result) || `HTTP ${response.status}`
                );
            }

            writeupForm.reset();

            document
                .getElementById("add-writeup-modal")
                .hidePopover();

            showToast(
                "Berhasil",
                "Write-up baru berhasil ditambahkan!",
                "success"
            );

            await fetchWriteups(searchInput.value.trim());

        } catch (error) {
            console.error("Error adding write-up:", error);

            showToast(
                "Gagal menambahkan write-up",
                error.message,
                "error"
            );

        } finally {
            submitButton.disabled = false;
        }
    });
}

// Memuat data saat halaman dibuka
fetchWriteups(searchInput.value.trim());

// Membuka modal edit dan memuat data dari API
async function openEditModal(writeupId) {
    const url = DETAIL_WRITEUP_URL.replace(
        "00000000-0000-0000-0000-000000000000",
        encodeURIComponent(writeupId)
    );

    try {
        const response = await fetch(url, {
            headers: {
                "Accept": "application/json",
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const writeup = await response.json();

        document.getElementById("edit-writeup-id").value = writeup.id;
        document.getElementById("edit-title").value = writeup.title || "";
        document.getElementById("edit-description").value = writeup.description || "";
        document.getElementById("edit-writeup-url").value = writeup.writeup_url || "";

        const modal = document.getElementById("edit-writeup-modal");
        if (modal && typeof modal.showPopover === "function") {
            modal.showPopover();
        }
    } catch (error) {
        console.error("Error loading write-up detail:", error);
        showToast("Gagal", "Tidak dapat memuat detail write-up.", "error");
    }
}

// PATCH: Mengirim pembaruan write-up ke API
const editWriteupForm = document.getElementById("edit-writeup-form");

if (editWriteupForm) {
    editWriteupForm.addEventListener("submit", async event => {
        event.preventDefault();

        const submitButton = editWriteupForm.querySelector(
            'button[type="submit"]'
        );
        submitButton.disabled = true;

        const writeupId = document.getElementById("edit-writeup-id").value;
        const url = DETAIL_WRITEUP_URL.replace(
            "00000000-0000-0000-0000-000000000000",
            encodeURIComponent(writeupId)
        );

        const payload = {
            title: document.getElementById("edit-title").value,
            description: document.getElementById("edit-description").value,
            writeup_url: document.getElementById("edit-writeup-url").value,
        };

        try {
            const response = await fetch(url, {
                method: "PATCH",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify(payload),
            });

            const result = await response.json().catch(() => ({}));

            if (!response.ok) {
                const message =
                    result.title?.[0] ||
                    result.description?.[0] ||
                    result.writeup_url?.[0] ||
                    result.detail ||
                    `HTTP ${response.status}`;
                throw new Error(message);
            }

            const modal = document.getElementById("edit-writeup-modal");
            if (modal && typeof modal.hidePopover === "function") {
                modal.hidePopover();
            }

            showToast(
                "Berhasil",
                "Write-up berhasil diperbarui!",
                "success"
            );

            await fetchWriteups(searchInput.value.trim());

        } catch (error) {
            console.error("Error updating write-up:", error);
            showToast(
                "Gagal memperbarui write-up",
                error.message,
                "error"
            );
        } finally {
            submitButton.disabled = false;
        }
    });
}
