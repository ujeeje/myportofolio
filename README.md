Nama : Jefry Acmal Dzikhrullah

NPM : 2506614795

Kelas : PBP A

# My Portofolio

My Portofolio adalah web portofolio pribadi saya berbasis Django.

## Tugas 1
1. Saya menggunakan elemen semantik HTML5 seperti `<section>` untuk menyusun struktur halaman portofolio ini. Elemen tersebut sangat membantu dalam membagi website statis ke dalam blok-blok konten yang terorganisir secara logis. Hal ini membuat kode menjadi lebih bersih serta mempermudah penerapan CSS pada setiap bagian spesifik.

Dalam membuat kerangka dasar file index.html, saya menggunakan bantuan AI secara bertahap untuk menyusun bagian Achievement, Experience, dan Skills dengan AI memberikan contoh kode ataupun template HTML-nya. Mengingat AI terkadang membuat struktur tag yang terlalu generik dan kurang sesuai dengan data personal saya (serta terkadang sulit untuk saya pahami), saya melakukan perbaikan manual seperti menyesuaikan nama atribut, nama class, dan menyusun ulang daftar-daftar item yang ingin saya masukkan.

2. Tantangan utama yang saya hadapi adalah proses memahami dan menerapkan berbagai macam gaya desain di CSS, karena saya masih cukup kesulitan jika harus menulis kodenya dari nol. Dalam mengevaluasi elemen yang perlu diubah posisinya, saya melihat bagian layout yang rumit seperti timeline zig-zag, yang kemudian disesuaikan menjadi satu sisi agar tetap rapi dan tidak terpotong di layar perangkat seluler. Sementara itu, prioritas ukuran diberikan pada kontainer utama dan teks agar strukturnya tetap proporsional serta nyaman dibaca di berbagai ukuran layar.

Untuk bagian CSS, saya menggunakan AI untuk membantu menuangkan gaya design saya ke dalam bentuk sintaks CSS, mengingat saya masih belum fasih menggunakan berbagai macam gaya desain di CSS yang sangat beragam. AI membantu merumuskan properti lanjutan seperti animasi pada section achivement, garis timeline pada section experiences dan susunan kotak pada section skilss. Akan tetapi, saya tetap melakukan banyak penyesuaian dan uji coba mandiri untuk merapikan tataletak tersebut. Hasil dari AI tidak sepenuhnya langsung "fit" pada website yang saya bangun ini.

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
