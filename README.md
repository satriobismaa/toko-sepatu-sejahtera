Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.  Membuat sebuah proyek Django baru.
    Pertama kali buat dan jalankan virtual environment di direktori toko-sepatu-sejahtera. Lalu buat sebuah txt (requirements.txt) yang berisi hal-hal yang ingin di install, salah satunya django. Setelah itu, jalankan "django-admin startproject toko_sepatu_sejahtera" yang akan membuat proyek django baru.

2.  Membuat aplikasi dengan nama main pada proyek tersebut.
    Sama seperti sebelumnya, pertama kali buat dan jalankan virtual environment di direktori toko-sepatu-sejahtera. Lalu jalankan "python manage.py startapp main" pada direktori toko-sepatu-sejahtera. Terakhir, daftarkan aplikasi main pada settings.py dengan menambahkan 'main' pada list INSTALLED_APPS

3.  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Pada berkas urls.py di direktori proyek, tambahkan fungsi include di bagian impor. Lalu tambahkan "path('', include('main.urls'))", pada list urlpatterns untuk bisa menghubungkan proyek ke aplikasi main

4.  Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
        name sebagai nama item dengan tipe CharField.
        price sebagai harga item dengan tipe IntegerField.
        description sebagai deskripsi item dengan tipe TextField.
        thumbnail sebagai gambar item dengan tipe URLField.
        category sebagai kategori item dengan tipe CharField.
        is_featured sebagai status unggulan item dengan tipe BooleanField.
    Ketika membuat aplikasi main, otomatis juga terbuat berkas models.py. Lalu tambahkan atribut-atribut tersebut pada berkas models.py yang sudah dibuat di dalam class Product.

5.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang   
    menampilkan nama aplikasi serta nama dan kelas kamu.
    Menambahkan fungsi ini pada views.py yang akan dikirimkan ke templates main.html ketika dipanggil
    def show_info(request):
        context = {
            'app_name': 'Toko Sepatu Sejahtera',
            'name': 'Bisma Zharfan Satryo Wibowo',
            'class': 'PBP B'
        }

        return render(request, "main.html", context)

6.  Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada     
    views.py.
    Pertama buat berkas urls.py di direktori aplikasi main. Lalu tambahkan kode ini
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_info, name='show_info'),
    ]
    Kode ini akan memanggil fungsi show_info di views.py jika url dengan path kosong (' ') direquest

7.  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses    
    oleh teman-temanmu melalui Internet. 
    Untuk melakukan deployment ke PWS, pertama login ke website PWS terlebih dahulu. Lalu, klik create new proyek dan tulis nama tokosepatusejahtera. Simpan credentials dari proyek tersebut. Lalu, copy isi dari berkas .env.prod ke environ di proyek tersebut. Tambahkan url PWS ke list allowed_host yang ada di settings.py. Terakhir, lakukan add, commit, dan push ke PWS dan masukkan credentials yang tadi sudah disimpan.



Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](image.png)
Urutan alur kerja Django adalah sebagai berikut:
1.  Pengguna mengetikkan URL di browser yang akan mengirimkan HTTP request ke server web
2.  HTTP request akan diterima oleh urls.py yang akan mencocokkan dengan pola URL dengan view yang tepat
3.  View akan menjalankan logika aplikasi, jika view membutuhkan untuk menulis atau membaca data maka  
    akan melibatkan interaksi dengan Model (models.py)
4.  Setelah diproses, view akan memanggil Template yang sesuai agar bisa ditampilkan dengan lebih 
    terstruktur dan rapih dalam bentuk .html
5.  Terakhir, Django akan mengirimkan HTTP Response dalam bentuk html yang pengguna bisa lihat di 
    browser mereka



Jelaskan peran settings.py dalam proyek Django!
settings.py adalah pusat konfigurasi Django yang mengatur database, aplikasi, keamanan, template, static files, middleware, dan berbagai pengaturan lain yang dibutuhkan agar proyek bisa berjalan dengan benar. Jadi setiap kali aplikasi Django dijalankan, Django akan membaca settings.py telebih dahulu untuk tahu bagaimana harus beroperasi.



Bagaimana cara kerja migrasi database di Django?
Pertama, ketika kita membuat misal class Product di Models.py, maka artinya kita ingin Django untuk membuat tabel Product dengan atribut-atributnya. Lalu, ketika kita menjalankan command "python manage.py makemigrations" setelah membuat Product di models.py, Django akan membaca perubahan pada models.py dan membuat file migration di folder migrations sesuai dengan perubahan tersebut. Setelah itu, ketika kita menjalankan "python manage.py makemigrations", Django akan mengeksekusi file migration tersebut ke database, dalam kasus ini, Django akan membuat tabel Product di database 



Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dipilih menjadi framework untuk permulaan pembelajaran ini, karena penggunaan bahasa Python yang menjadikannya lebih mudah dimengerti. Selain itu Django juga sudah lengkap dari awal dengan banyak fitur bawaan. Django juga dipilih, karena lebih terstruktur, aman, didukung komunitas besar, dan tetap relevan di industri.



Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Kalau dari saya, tidak ada, karena dari web tutorial nya sudah sangat jelas dari step-by-step nya, lalu asisten dosennya pun selalu ada buat ngebantu kita kalo ada yang bermasalah. 