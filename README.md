Nama : Jefry Acmal Dzikhrullah

NPM : 2506614795

Kelas : PBP A

# My Portofolio

My Portofolio adalah web portofolio pribadi saya berbasis Django.

## Tugas 1
1. Saya menggunakan elemen semantik HTML5 seperti `<section>` untuk menyusun struktur halaman portofolio ini. Elemen tersebut sangat membantu dalam membagi website statis ke dalam blok-blok konten yang terorganisir secara logis. Hal ini membuat kode menjadi lebih bersih serta mempermudah penerapan CSS pada setiap bagian spesifik. Dalam membuat kerangka dasar file index.html, saya menggunakan bantuan AI secara bertahap untuk menyusun bagian Achievement, Experience, dan Skills dengan AI memberikan contoh kode ataupun template HTML-nya. Mengingat AI terkadang membuat struktur tag yang terlalu generik dan kurang sesuai dengan data personal saya (serta terkadang sulit untuk saya pahami), saya melakukan perbaikan manual seperti menyesuaikan nama atribut, nama class, dan menyusun ulang daftar-daftar item yang ingin saya masukkan.

2. Tantangan utama yang saya hadapi adalah proses memahami dan menerapkan berbagai macam gaya desain di CSS, karena saya masih cukup kesulitan jika harus menulis kodenya dari nol. Dalam mengevaluasi elemen yang perlu diubah posisinya, saya melihat bagian layout yang rumit seperti timeline zig-zag, yang kemudian disesuaikan menjadi satu sisi agar tetap rapi dan tidak terpotong di layar perangkat seluler. Sementara itu, prioritas ukuran diberikan pada kontainer utama dan teks agar strukturnya tetap proporsional serta nyaman dibaca di berbagai ukuran layar. Untuk bagian CSS, saya menggunakan AI untuk membantu menuangkan gaya design saya ke dalam bentuk sintaks CSS, mengingat saya masih belum fasih menggunakan berbagai macam gaya desain di CSS yang sangat beragam. AI membantu merumuskan properti lanjutan seperti animasi pada section achivement, garis timeline pada section experiences dan susunan kotak pada section skilss. Akan tetapi, saya tetap melakukan banyak penyesuaian dan uji coba mandiri untuk merapikan tataletak tersebut. Hasil dari AI tidak sepenuhnya langsung "fit" pada website yang saya bangun ini.

3. Batasan utama yang saya rasakan saat menggunakan web statis murni adalah kesulitan dalam menggabungkan animasi slide otomatis pada bagian achievement agar tetap bisa digeser atau di-swipe secara manual secara bersamaan. Berdasarkan batasan tersebut, fungsionalitas dinamis yang paling ingin saya persiapkan pada iterasi proyek selanjutnya adalah membuat setiap item seperti achievement, experience, atau skills dapat diklik untuk membuka tampilan modal atau halaman detail yang lebih luas dan mendetail mengenai item tersebut.

Riwayat penggunaan generative AI: https://share.gemini.google/exYx9S0VjfGT

## Tugas 2

1. Saat sebuah halaman web diakses, prosesnya melewati beberapa lapisan pemrosesan agar data yang tepat bisa dirender. Ketika saya membuka URL halaman portofolio baru di browser, request tersebut pertama kali akan ditangkap oleh urls.py pada tingkat proyek. File ini bertugas sebagai pengarah lalu lintas utama yang kemudian meneruskan request ke urls.py di tingkat aplikasi. Di dalam urls.py aplikasi, path URL tersebut dicocokkan dengan sebuah view tertentu. View ini lalu mengambil alih pemrosesan dengan meminta data yang dibutuhkan dari database melalui perantara model. Setelah model memberikan data yang dicari, view akan memasukkan data tersebut ke dalam context dictionary dan mengirimkannya ke template. Terakhir, template merender data dinamis tersebut ke dalam struktur HTML dan menampilkannya sebagai halaman yang utuh di browser saya.

2. Menyimpan informasi langsung ke dalam file HTML akan menyulitkan ketika konten portofolio mulai bertambah banyak. Menyimpan data pada model jauh lebih baik daripada menuliskannya secara hard-coded di dalam template karena alasan skalabilitas dan kemudahan pemeliharaan. Dengan menggunakan model, saya bisa menambah, mengedit, atau menghapus data proyek kapan saja melalui panel admin atau shell tanpa perlu menyentuh dan membongkar kode HTML sama sekali. Sebaliknya, jika data di-hardcode, setiap kali ada tulisan writeup baru, saya harus mengubah file template-nya secara manual, yang tentu tidak efisien dan rentan memicu error pada antarmuka. 

3. Django tidak bisa secara otomatis menyinkronkan perubahan pada kode Python dengan struktur tabel database tanpa ada instruksi yang menjembatani keduanya. Perbedaan utamanya adalah perintah `makemigrations` berfungsi untuk memindai setiap perubahan yang saya tulis pada file models.py dan mencatatnya ke dalam sebuah file draf skema migrasi baru. Sementara itu, perintah `migrate` berfungsi untuk membaca file draf migrasi tersebut dan benar-benar menerapkan perubahannya ke dalam database. 

Riwayat penggunaan generative AI: https://share.gemini.google/Mip5oJ1MldXQ

## Tugas 3

### Perubahan Mingguan
- Refactor berkas HTML yang identik dengan melakukan extend dari root html template
- Membuat Modelform untuk bagian Experience
- Membuat view JSON untuk bagian Experience
- Mengubah show_experience agar menggunakan JSON dan deserialized
- Membuat view create, update, delete experience
- Membuat template form experience


### Pertanyaan Reflektif
1. Dalam pengembangan web dengan Django, kita sering berurusan dengan pengumpulan data dari pengguna yang akan memakan waktu panjang jika formulir dan sistem validasinya dibuat satu per satu secara manual. Oleh karena itu, kita menggunakan ModelForm agar Django secara otomatis membuatkan elemen HTML sekaligus mengatur validasi dan penyimpanan datanya berdasarkan definisi model yang sudah ada di database. Penambahan `{% csrf_token %}` diwajibkan pada form tersebut sebagai mekanisme keamanan untuk memastikan pengiriman data benar-benar berasal dari pengguna di situs web kita, sehingga dapat mencegah serangan pemalsuan dari luar.

2. JSON menjadi lebih disukai dalam pengembangan modern karena memiliki struktur penulisan yang jauh lebih ringkas sehingga proses pengiriman datanya lebih hemat bandwidth dan lebih cepat daripada XML. Selain itu, JSON juga merupakan bagian asli dari lingkungan JavaScript yang memungkinkan browser untuk langsung memproses datanya.

3. Ketika ada permintaan untuk melihat data portofolio, fungsi view mula-mula akan mencari dan mengambil kumpulan data tersebut dari database yang pada saat itu wujudnya masih berupa objek bawaan dari Python. Karena protokol HTTP hanya bisa menghantarkan informasi dalam bentuk teks, kita harus melakukan proses serialization terlebih dahulu guna menerjemahkan objek Python tadi ke dalam wujud teks terstruktur. Setelah datanya berhasil diubah menjadi teks JSON, barulah view membungkusnya ke dalam respons HTTP.

### Riwayat Penggunaan GenAI

https://chatgpt.com/s/cx_6ab155328e68819194a9d0aa63d669bb

## Tugas 4

### Perubahan Mingguan
- Membuat otentifikasi register, login, dan logout
- Menambahkan cookie `last_login` saat login pengguna dan menghapus cookie-nya saat logout
- Membuat fitur interaktif bintang untuk writeup favorit pengguna
- Otorisasi role guest yang hanya bisa melihat portofolio
- Otorisasi role registered user yang bisa melihat portofolio dan memberi bintang
- Otorisasi role editor yang bisa mengupdate data di section experience

### Riwayat Penggunaan GenAI
Pada tugas 4 ini saya menggunakan AI untuk memeriksa otorisasi editor apakah sudah berjalan dengan benar, meminta penjelasan lebih lanjut pada aksi penambahan relasi ManyToManyField ke model User, serta memeriksa apakah perubahan yang dilakukan sudah memenuhi ketentuan dan website bisa berfungsi sebagaimana mestinya pada untuk semua fitur. Saya menyoroti AI masih belum bisa melakukan debugging web dengan baik terlebih direktori dan file yang diperlukan pada projek web portofolio ini yang semakin kompleks. Saya tetap melakukan debugging manual dengan juga berkonsultasi pada AI untuk menemukan solusinya.

- https://chatgpt.com/s/cx_6aba872ac97c81919073e0d477152fc1

## Tugas 5

### Perubahan Mingguan
- Mengubah alur pemuatan data daftar writeup CTF menjadi asinkron menggunakan AJAX untuk mengambil data dari endpoint JSON tanpa reload halaman.
- Menambahkan handling User Interdace untuk kondisi loading, data kosong, dan error saat memuat data dari server.
- Menerapkan fitur pencarian writeup via AJAX dengan teknik debouncing
- Mengimplementasikan pengiriman data form dengan AJAX POST
- Menambahkan notifikasi toast untuk memberikan feedback (status berhasil, gagal, atau pesan error validasi) kepada pengguna.
- Menerapkan escaping teks pada JavaScript dan sanitasi input menggunakan strip_tags pada level ModelForm di sisi server.

### Pertanyaan Reflektif
1. Pada fitur pencarian, setiap karakter yang diketik oleh pengguna dapat memicu pengiriman permintaan ke server secara beruntun. Untuk mengelola hal tersebut, digunakan teknik debouncing, yaitu teknik untuk menunda pengeksekusian sebuah fungsi hingga suatu jeda waktu berlalu tanpa adanya input baru. Teknik ini diterapkan pada AJAX karena membuat pencarian lebih efisien dengan cara memastikan permintaan hanya dikirim ke server setelah pengguna benar-benar berhenti mengetik sejenak, sehingga mencegah terjadinya pengiriman permintaan data berulang-ulang dari setiap huruf yang diketik.

2. Saat memanggil data menggunakan fungsi `fetch()`, fungsi tersebut tidak langsung menghasilkan data melainkan mengembalikan sebuah Promise. Fungsi utama dari penggunaan keyword await adalah untuk memerintahkan program agar "menunggu" Promise tersebut selesai diproses secara penuh sebelum melanjutkan eksekusi ke baris kode berikutnya. Jika await tidak digunakan, Promise tersebut akan dibiarkan tetap berjalan di belakang layar sementara baris kode di bawahnya akan langsung dieksekusi tanpa menunggu hasil pengambilan data tersebut tersedia

3. Serangan XSS (Cross-Site Scripting) adalah sebuah jenis serangan di mana pihak penyerang berhasil menyisipkan kode JavaScript berbahaya ke dalam suatu halaman web, dan kemudian tanpa disengaja ikut dijalankan pada browser pengguna lain. Data yang ditampilkan via JavaScript jauh lebih rentan terhadap XSS karena data sering kali disisipkan secara langsung ke halaman web tanpa perlindungan seperti escaping. Perlindungan escaping merupakan proses pengubahan karakter-karakter khusus HTML (seperti tanda < dan >) menjadi teks biasa (seperti &lt; dan &gt;). Tanpa adanya proses ini, browser akan menafsirkan karakter tersebut sebagai tag HTML atau kode sungguhan yang harus dieksekusi. Hal ini berbeda dengan template Django yang sudah memiliki mekanisme auto-escaping bawaan untuk mengubah karakter khusus HTML menjadi teks biasa, sehingga tag HTML yang berbahaya tersebut tidak akan dieksekusi oleh browser sebagai kode.

### Riwayat Penggunaan GenAI
Pada tugas 5 ini saya menggunakan AI untuk memandu saya dalam mengimplementasikan AJAX, Debouncing, Toast Notification, dan XSS Protection. Saya juga meminta penjelasan lebih lanjut terkait tahap-tahap yang perlu saya lakukan dan efeknya pada projek saya ini. Selain itu, saya juga menggunakan AI untuk memeriksa apakah perubahan yang dilakukan sudah memenuhi ketentuan dan website bisa berfungsi sebagaimana mestinya pada untuk semua fitur. Saya menyoroti AI masih belum bisa melakukan debugging web dengan baik terlebih direktori dan file yang diperlukan pada projek web portofolio ini yang semakin kompleks. Saya tetap melakukan debugging manual dengan juga berkonsultasi pada AI untuk menemukan solusinya.

- https://chatgpt.com/s/cx_6ac3bad648d08191a01cc1a26058cd99 

## Tugas 6

### Perubahan Mingguan
- Menambahkan Django REST Framework ke dependensi dan settings, serta mendaftarkan rute API di bawah prefix api/v1/.
- Membuat CTFWriteupSerializer dengan field read-only star_count, is_starred, dan starred_by_names, serta sanitasi input menggunakan strip_tags untuk mencegah XSS.
- Membuat permission class dengan 4 peran: Pengunjung (baca), Pengguna Terdaftar (baca dan star), Editor (baca, star, PUT/PATCH), dan Superuser (akses penuh CRUD).
- Mengimplementasikan API view berbasis fungsi untuk list (dengan pencarian ?title=), detail, dan toggle star, dengan status kode HTTP yang sesuai.
- Mengubah halaman write-up menjadi asinkron dengan fetch() untuk fitur Read, Search (debouncing), Create, Star, Edit (PATCH), dan Delete tanpa reload halaman.
- Menyertakan header X-CSRFToken pada request mutasi, menambahkan notifikasi toast untuk sukses dan error (400/403), serta menerapkan escaping teks pada JavaScript.
- Menulis unit test dengan APITestCase untuk akses tiap peran, validasi dan sanitasi input, toggle star, dan proteksi CSRF.


### Pertanyaan Reflektif
1. Menurut saya, REST (Representational State Transfer) bisa dikatakan seperangkat aturan untuk merancang API di web. Aturan ini mengatur bagaimana URL disusun, method HTTP dipakai, dan status code dikembalikan. API yang mengikuti aturan ini disebut RESTful. JSON hanya menentukan format data yang dikirim, sedangkan REST menentukan struktur komunikasinya. Karena itu, API yang mengembalikan JSON belum tentu RESTful. Misalnya, ada API yang menerima semua tindakan lewat satu URL dengan POST, lalu membalas dengan JSON. API seperti itu tidak mengikuti aturan REST. Ada tiga prinsip REST yang kita terapkan. 
    1) Setiap data diperlakukan sebagai resource dengan URL sendiri. Contohnya `/api/v1/ctf-writeups/` untuk kumpulan write-up dan `/api/v1/ctf-writeups/<uuid>/` untuk satu write-up. 
    2) Tindakan ditentukan oleh HTTP method, bukan oleh URL. GET untuk membaca, POST untuk membuat, PUT atau PATCH untuk mengubah, dan DELETE untuk menghapus. Dengan begitu, kita tidak perlu membuat URL seperti `/add-ajax/` atau `/delete/`. 
    3) Server mengembalikan status code yang sesuai dengan hasilnya, misalnya 201 untuk data yang berhasil dibuat dan 404 untuk data yang tidak ditemukan. 
Selanjutnya, PUT dan PATCH sama-sama dipakai untuk mengubah data, tetapi cakupannya berbeda. PUT mengganti seluruh resource, sehingga semua field harus dikirim ulang. PATCH hanya mengubah field yang dikirim. Oleh karena itu, PUT cocok untuk form edit yang menampilkan semua field. Sebaliknya, PATCH cocok untuk perubahan kecil, misalnya modal edit yang hanya mengganti judul write-up.

2. Serializer adalah komponen di Django REST Framework, yaitu toolkit di atas Django untuk membangun web API. Tugas serializer adalah menerjemahkan data antara objek model Django dan format yang dipakai klien, yaitu JSON. Pada serialization, misalnya saat GET, serializer mengubah objek model menjadi data Python yang kemudian dirender menjadi JSON. Pada deserialization, misalnya saat POST atau PATCH, serializer membaca JSON dari request dan mengubahnya menjadi data Python. Data itu divalidasi dengan `is_valid()`, lalu disimpan ke database dengan `save()`. Pada Tutorial 05, semua itu dikerjakan secara manual. `get_projects_json` membuat dictionary untuk setiap objek lewat perulangan. Lalu `create_project_ajax` memvalidasi input dengan form dan menentukan status HTTP sendiri. Pola ini harus ditulis ulang setiap ada model baru.  Serializer menyederhanakannya dengan cukup ditulis sekali di satu class. 

3. Autentikasi memeriksa “siapa pengirim request ini?”. Pada tahap ini, `SessionAuthentication` membaca session dan mengisi request.user. Jika pengguna belum login, request.user berisi AnonymousUser. Setelah identitas diketahui, otorisasi menjawab pertanyaan “apakah pengirim ini boleh melakukan tindakan tersebut?”. Tahap ini dikerjakan oleh permission class. Contohnya,  `IsPortfolioOwnerOrEditorOrReadOnly` hanya mengizinkan pengunjung membaca. Editor boleh membaca serta melakukan PUT dan PATCH. Superuser boleh melakukan semua operasi. Pemeriksaan ini harus dilakukan di server karena menyembunyikan tombol di template hanya mengubah tampilan, sedangkan otorisasinya tidak berubah. Siapa pun tetap bisa mengirim request langsung ke endpoint lewat fetch atau curl tanpa menekan tombol apa pun. 

4. `SessionAuthentication` mengenali pengguna lewat cookie session yang disimpan browser setelah login. Browser otomatis menyertakan cookie ini pada setiap request ke domain yang sama, termasuk bisa dari request yang dikirim diam-diam dari website lain. Akibatnya, website seorang attacker bisa membuat request DELETE atas nama kita yang sedang login. Serangan ini disebut CSRF. Karena itu, request yang mengubah data harus membawa token CSRF di header X-CSRFToken. Website penyerang tidak bisa membaca token tersebut, sehingga request palsunya direject dengan 403. Test yang memakai `force_authenticate` langsung menetapkan pengguna tanpa login dan session, sehingga pemeriksaan CSRF terlewati. Oleh karena itu, test harus memakai `APIClient(enforce_csrf_checks=True)` dan `.login()` agar pemeriksaan CSRF berjalan seperti di browser.

### Riwayat Penggunaan GenAI
Pada tugas 6 ini saya menggunakan AI untuk memeriksa checklist yang ada pada ketentuan tugas, sehingga saya bisa memastikan tidak ada bagian yang terlewat. Saya juga menggunakan AI untuk membantu mengimplementasikan fitur menyediakan cara mengubah data via PUT atau PATCH dari halaman, yaitu modal edit dan tombol Edit yang memanggil endpoint API. Selain itu, saya menggunakan AI untuk memeriksa apakah perubahan yang dilakukan sudah memenuhi ketentuan dan website bisa berfungsi sebagaimana mestinya untuk semua fitur. Saya menyoroti bahwa AI masih belum bisa melakukan debugging web dengan baik, terlebih karena direktori dan file pada projek web portofolio ini semakin kompleks. Saya tetap melakukan debugging manual sambil berkonsultasi dengan AI untuk menemukan solusinya.

## Panduan Setup

1. Masuk ke direktori project.

```bash
cd myportofolio
```

2. Buat virtual environment.

```bash
python -m venv env
```

3. Aktifkan virtual environment.

Untuk Windows:

```bash
env\Scripts\activate
```

Untuk Linux/Mac:

```bash
source env/bin/activate
```

4. Install dependencies dari `requirements.txt`.

```bash
pip install -r requirements.txt
```

5. Buat file `.env` jika belum ada.

Untuk development lokal, isi dengan:

```env
PRODUCTION=False
```

Untuk production dengan PostgreSQL, isi dengan:

```env
PRODUCTION=True
DB_NAME=nama_database
DB_USER=user_database
DB_PASSWORD=password_database
DB_HOST=host_database
DB_PORT=port_database
SCHEMA=public
```

6. Jalankan migrasi database.

```bash
python manage.py migrate
```

7. Jika ingin mengakses Django Admin, buat superuser.

```bash
python manage.py createsuperuser
```

Setelah setup selesai, project siap dijalankan.

## Panduan Menjalankan Project

8. Jalankan development server dengan perintah berikut:

```bash
python manage.py runserver
```

Setelah server berjalan, buka aplikasi di browser melalui:

```text
http://127.0.0.1:8000/
```

## Panduan Test

Untuk menjalankan seluruh test Django, gunakan perintah berikut:

```bash
python manage.py test
```
