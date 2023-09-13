Nama: Anastasia Keisha Bella Arianne Pepe

NPM: 2206082272

Kelas: PBP F

Link adaptable: https://bookstore.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

a. Membuat sebuah proyek Django baru.
    - Membuat direktori baru (toko_buku) dan masuk ke dalamnya
    - Membuka terminal dan membuat virtual menjalankan perintah "python -m venv env"
    - Mengaktifkan virtual environment dengan mennjalankan perintah "env\Scripts\activate.bat". Virtual environment akan aktif yang ditandai dengan (env) di baris input terminal
    - Di dalam direktori toko_buku, dibuat berkas requirements.txt dan menambahkan beberapa dependecies
    - Pasang dependencies dengan menjalankan perintah "pip install -r requirements.txt"
    - Membuat proyek Django dengan nama toko_buku dengan perintah "django-admin startproject shopping_list ."
    - Untuk konfigurasi proyek dan menjalankan server, ditambahkan "*" pada ALLOWED_HOST di settings.py untuk keperluan deployment dan mengizinkan akses dari semua host
    - Menjalankan server Django dengan perintah "python manage.py runserver"
    - Membuka http://localhost:8000 pada peramban web dan terlihat animasi roket, maka aplikasi Django sudah berhasil dibuat
    - Menghentikan server dengan CTRL + C
    - Menonaktifkan virtual environment dengan perintah "deactivate"
    - Membuat repositori GitHub baru (toko-buku) dengan visibilitas public
    - Menginisiasi direktori toko_buku sebagai repositori Git
    - Menambahkan dan mengisi berkas .gitignore untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git
    - Melakukan add, commit, push dari direktori lokal

b. Membuat aplikasi dengan nama main pada proyek tersebut.
    - Membuka direktori proyek toko_buku yang sebelumnya sudah dibuat
    - Membuka terminal dengan direktori kerja saat ini adalah direktori utama toko_buku
    - Mengaktifkan virtual environment dengan menjalankan perintah "env\Scripts\activate.bat"
    - Membuat aplikasi baru bernama "main" dengan menjalankan perintah "python manage.py startapp main"
    - Mendaftarkan aplikasi main ke dalam proyek dengan membuka berkas settings.py di dalam direktori proyek toko_buku dan menambahkan 'main' ke variabel "INSTALLED_APPS" untuk mendaftarkan aplikasi main ke dalam proyek toko_buku 

c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
= Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
    - Membuat direktori baru bernama templates dalam direktori aplikasi main
    - Membuat dan mengisi berkas main.html sesuai data yang diinginkan dan diperlukan
    - Memeriksa tampilan dasar html dengan membuka main.html di peramban web
    - Mengubah berkas models.py dalam aplikasi main untuk mendefinisikan model baru dengan atribut atau field yang diinginkan dan diperlukan
    - Membuat migrasi model dengan menjalankan perintah "python manage.py makemigrations" 
    - Menjalankan perintah "python manage.py migrate" untuk menerapkan migrasi ke dalam basis data lokal

d. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Membuka berkas views.py di dalam berkas aplikasi main
    - Menambahkan baris-baris impor "from django.shortcuts import render" di bagian paling atas berkas untuk mengimpor fungsi render dari modul django.shortcuts yang akan digunakan untuk me-render tampilan html dengan menggunakan data yang diberikan. 
    - Menambahkan fungsi show_main(request) di bawah impor dan mengisi dictionary context yang berisi data yang akan dikirimkan ke tampilan serta me-return render(request, "main.html", context) untuk me-rendder tampilan main.html dengan menggunakan fungsi render
    - Mengubah template main.html agar dapat menampilkan data yang telah diambil dari model dengan mengubah variabel yang sebelumnya dibuat secara statis menjadi kode Django yang sesuai untuk menampilkan data

e. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    - Membuat berkas urls.py di dalam direktori main
    - Mengisi urls.py dengan kode yang sesuai untuk mengartur rute url yang terkait dengan aplikasi main
    - Impor path dari django.urls untuk mendefinisikan pola url
    - Menggunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses
    - Nama pada app_name untuk memberikan nama unik pada pola url dalam aplikasi
    - Selanjutnya, buka berkas urls.py di dalam direktori proyek toko_buku, bukan yang ada dalam direktori aplikasi main
    - Mengimpor fungsi include dari django.urls
    - Menambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns
    - Menjalankan pryek Django dengan perintah "python manage.py runserver"
    - Membuka http://localhost:8000/main/ di peramban web untuk melihan halaman yang sudah dibuat

f. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Login ke Adaptable.io menggunakan akun GitHub yang digunnakan untuk membuat proyek toko_buku
    - Menekan tombol "New App"
    - Memilih "Connect an Existing Repository"
    - Menghubungkan Adaptable.io dengan GitHub dan memilih "All Repositories" pada proses instalasi
    - Memilih repositori proyek toko-buku sebagai basis aplikasi yang akan di deploy
    - Memilih branch main untuk dijadikan sebagai deployment branch
    - Memilih "Python App Template" sebagai template deployment
    - Memilih "PostgreSQL" sebagai tipe basis data yang akan digunakan
    - Menyesuaikan versi python dengan spesifikasi aplikasi
    - Pada bagian "Start Command" dimasukkan perintah "python manage.py migrate && gunicorn toko_buku.wsgi"
    - Memasukkan nama aplikasi yang akan menjadi nama domain situs web aplikasi
    - Centang bagian "HTTP Listener on PORT" dan klik  "Deploy App" untuk memulai proses deployment aplikasi

g. Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy
    - Menambahkan READM.md di direktori utama toko_buku
    - Melakukan add, commit, push

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](bagan.png)
Penjelasan:
    - User membuat request ke web aplikasi berbasi Django
    - Request tersebut diteruskan ke Django
    - Django mengidentifikasi path url (urls.py mengatur rute url terkait)
    - View menggunakan model untuk memproses request dan meneruskannya ke template (views.py mengatur logika bisnis aplikasi dan menangani request yang diterima melalui url dengan mengambil data dari model, memproses data itu, kemudian memberikan response)
    - Model digunakan untuk mengakses dan menyimpan data ke dalam basis data (models.py)
    - Template akan menghasilkan response yang sesuai dengan menampilkan data yang diterima dari database, seperti berkas html 
    - Berkas html diteruskan ke web client

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan karena proyek dapat membutuhkan dependencies yang berbeda-beda setiap proyeknya. Oleh karena itu, dibutuhkan virtual environment untuk menjalankannya tanpa merubah konfigurasi sistem operasi yang kita pakai agar menghindari masalah/crash.

Kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi dapat memungkinkan terjadinya masalah konlfik versi dan kesulitan dalam mengelola dependencies.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
a. MVC (Model-View-Controller) -> Sebuah pola desain arsitektur yang digunakan dalam pengembangan web  dengan cara memisahkan kode menjadi tiga bagian, yaitu Model, View, dan Controller.
    - Model: Menyimpan data dan logika bisnis 
    - View: Menampilkan data kepada pengguna dalam bentuk GUI (Graphical User Interface)
    - Controller: Menghubungkan dan mengatur model serta view
b. MVT (Model-View-Template) -> Sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
    - Model: Menyimpan data dan logika aplikasi.
    - View: Menampilkan data dari model dan menghubungkannya dengan template.
    - Template: Menentukan tampilan antarmuka pengguna.
c. MVVM (Model-View-ViewModel) -> Sebuah arsitektur pembuatan aplikasi berbasi GUI yang berfokus pada peisahan antara lofika bisnis dan tampilan aplikasi.
    - Model: Menyimpan data dan logika bisnis 
    - View: Menampilkan data ke pengguna, tetapi tidak memiliki logika bisnis
    - ViewModel: Perantara antara Model dan View. Berinteraksi dengan model dimana data yang ada akan diteruskan ke View

Perbedaan:
    - MVC -> umum digunakan dalam pengembangan web tradisional, tampilannya dikontrol oleh View
    - MVT -> khusus digunakan dalam Django, penggunaan template yang berperan dalam menampilkan data
    - MVVM -> umum digunakan dalam pengembangan aplikasi berbasis dekstop dan mobile, menggunakan ViewModel sebagai perantara sehingga tampilan antarmuka pengguna lebih dinamis