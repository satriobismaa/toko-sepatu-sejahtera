
<details>
<Summary><b>Tugas 2</b></Summary>

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
<img src="images/image.png" alt="Foto" width="700">

Urutan alur kerja Django adalah sebagai berikut:
1.  Pengguna mengetikkan URL di browser yang akan mengirimkan HTTP request ke server web
2.  HTTP request akan diterima oleh urls.py yang akan mencocokkan dengan pola URL dengan view yang tepat
3.  View akan menjalankan logika aplikasi, jika view membutuhkan untuk menulis atau membaca data maka  
    akan melibatkan interaksi dengan Model (models.py)
4.  Setelah diproses, view akan memanggil Template yang sesuai agar bisa ditampilkan dengan lebih 
    terstruktur dan rapih dalam bentuk .html
5.  Terakhir, Django akan mengirimkan HTTP Response dalam bentuk html yang pengguna bisa lihat di 
    browser mereka
Reference: PPT 02 - Introduction to The Internet and Web Framework


Jelaskan peran settings.py dalam proyek Django!
settings.py adalah pusat konfigurasi Django yang mengatur database, aplikasi, keamanan, template, static files, middleware, dan berbagai pengaturan lain yang dibutuhkan agar proyek bisa berjalan dengan benar. Jadi setiap kali aplikasi Django dijalankan, Django akan membaca settings.py telebih dahulu untuk tahu bagaimana harus beroperasi.



Bagaimana cara kerja migrasi database di Django?
Pertama, ketika kita membuat misal class Product di Models.py, maka artinya kita ingin Django untuk membuat tabel Product dengan atribut-atributnya. Lalu, ketika kita menjalankan command "python manage.py makemigrations" setelah membuat Product di models.py, Django akan membaca perubahan pada models.py dan membuat file migration di folder migrations sesuai dengan perubahan tersebut. Setelah itu, ketika kita menjalankan "python manage.py makemigrations", Django akan mengeksekusi file migration tersebut ke database, dalam kasus ini, Django akan membuat tabel Product di database 



Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dipilih menjadi framework untuk permulaan pembelajaran ini, karena penggunaan bahasa Python yang menjadikannya lebih mudah dimengerti. Selain itu Django juga sudah lengkap dari awal dengan banyak fitur bawaan. Django juga dipilih, karena lebih terstruktur, aman, didukung komunitas besar, dan tetap relevan di industri.



Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Kalau dari saya, tidak ada, karena dari web tutorial nya sudah sangat jelas dari step-by-step nya, lalu asisten dosennya pun selalu ada buat ngebantu kita kalo ada yang bermasalah. 


</details>

<details>
<Summary><b>Tugas 3</b></Summary>
<ol>
    <li>
    Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data Delivery dibutuhkan dalam sebuah platform untuk
        <ol> 
            <li>Memungkinkan adanya interaksi antar komponen, yaitu dengan data delivery, komponen-komponen pada platform bisa saling bertukar informasi, misal dari frontend ke backend dan begitupun sebaliknya</li>
            <li>Menambah user experience, yaitu data delivery memungkinkan respon kepada pengguna dengan cepat dan data yang juga up-to-date</li>
            <li>Menjamin konsistensi data antar setiap komponen pada platform sehingga tidak ada data pada platform yang keliru</li>
            <li>Platform bisa terhubung ke layanan eksternal dengan mengirimkan data lintas sistem yang juga bisa menambah user experience</li>
            <li>Dengan data delivery, memungkinkan data atau informasi yang dikirimkan tidak hanya cepat sampai, tetapi juga aman dan andal</li>
        </ol>
    </li>
    <li>
    Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    XML dan JSON memiliki keunggulan dan kelemahannya masing-masing. Format XML lebih baik jika data membutuhkan struktur yang lebih kompleks, metadata, atau standar formal (contoh: dokumen hukum, konfigurasi enterprise, SOAP). Sedangkan JSON lebih baik untuk digunakan pada aplikasi web/mobile modern, API, atau sistem yang butuh kecepatan dan efisiensi. JSON lebih populer dikarenakan itu, 
        <ol>
            <li>JSON lebih ringan dan cepat diproses dibanding XML</li>
            <li>Struktur JSON mirip dengan objek di JavaScript, sehingga lebih mudah dipahami oleh developer web</li>
            <li>JSON bisa langsung digunakan di JavaScript tanpa perlu parsing tambahan</li>
            <li>API modern lebih banyak menggunakan JSON sebagai format data utama</li>
            <li>JSON lebih efisien untuk pertukaran data di aplikasi web/mobile yang butuh kecepatan</li>
        </ol>
    </li>
    <li>
    Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() digunakan untuk memvalidasi data yang diinput user, seperti:
        <ol>
            <li>Memeriksa apakah semua field yang diinput sudah sesuai, contohnya 'IntegerField(min_value=1)' yang jika tidak sesuai maka method akan mengembalikan false</li>
            <li>Menjalankan validasi built-in maupun custom, seperti email harus valid dan angka sesuai dengan range</li>
            <li>Mengisi 'cleaned_data' jika valid , yaitu jika form valid, 'form.cleaned_data' akan berisi data yang sudah dibersihkan dan siap dipakai (misalnya disimpan ke database).</li>
        </ol>
    Kita membutuhkan method tersebut untuk keamanan, yaitu agar input dari user dicek terlebih dahulu sebelum diproses. Selain itu, method ini juga dibutuhkan untuk memastikan data yang masuk sudah sesuai format. Terakhir, dengan adanya method ini memudahkan kita sebagai developer untuk memvalidasi input, tanpa mulai dari 0
    </li>
    <li>
    Mengapa kita membutuhkan 'csrf_token' saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan 'csrf_token' pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Fungsi utama dari 'csrf_token' adalah untuk memastikan bahwa request POST (misalnya ketika login ke akun) benar-benar pengguna sah yang menggunakan website kita, bukan pihak dari website lain yang menyamar. Jika kita tidak menambahkan 'csrf_token', maka aplikasi menjadi:
        <ol>
        <li>Menjadi rentan terhadap serangan csrf, yaitu penyerang dapat membuat website yang berbahaya dan diam-diam mengirim request POST ke website kita atas nama pengguna yang ingin login</li>
        <li>Tidak mempunyai validasi keaslian request, server tidak bisa tahu apakah request POST datang dari form asli di website kita atau dari pihak ketiga.</li>
        <li>Menambah resiko manipulasi data, misalnya: ubah password, kirim pesan, bahkan transfer saldo bisa dilakukan tanpa sepengetahuan user.</li>
        </ol>
    Penyerang dapat memanfaatkan hal ini dengan membuat website palsu (misal kita login ke bank.com (sudah ada session/cookie yang aktif)), lalu di website palsu itu ada form tersembunyi yang mengirim request POST ke bank.com untuk transfer uang ke akun penyerang.
    Kalau kita (yang sedang login di bank.com) tanpa sadar mengunjungi situs palsu itu:
        1. Browser otomatis mengirim cookie session bank.com + request POST ke server bank.com.
        2. Server mengira itu request sah dari kita.
        3. Uang kita bisa ditransfer ke akun penyerang tanpa kita tahu.
    Dengan csrf_token, serangan ini gagal, karena server akan mengecek apakah request berisi token valid. Situs palsu tidak bisa menebak token unik tersebut.
    </li>
    <li>
        Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
        <ol>
            <li>Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
            Fungsi untuk melihat semua data yang sudah ditambahkan:
            Membuat dua fungsi baru yang menerima parameter request dengan nama 'show_xml' dan 'show_json', serta membuat sebuah variabel di dalam kedua fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product, yaitu 'product_list = Product.objects.all()'. Lalu, Tambahkan return function yang berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter 'content_type="application/json"' pada fungsi json dan 'content_type="application/xml"' pada fungsi XML
            Fungsi untuk melihat data sesuai id yang diinginkan:
            Membuat dua fungsi baru yang menerima parameter request dan news_id dengan nama show_xml_by_id dan show_json_by_id, serta membuat variabel di dalam kedua fungsi tersebut yang menyimpan hasil hasil query dari data dengan id tertentu yang ada pada Product, yaitu 'product_item = Product.objects.filter(pk=product_id)'pada fungsi XML dan 'product_item = Product.objects.get(pk=product_id)' pada fungsi JSON. Lalu tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON). Setelah itu, tambahkan try except pada kedua fungsi untuk ketika id tidak ditemukan.
            Terakhir untuk keempat fungsi tambahkan juga import semua fungsi pada urls.py dan buat pathnya masing-masing
            </li>
            <li>
            Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
            Setelah membuat keempat fungsi, maka pertama import dulu semua fungsi tersebut ke urls.py pada direktori main. Setelah itu buat path setiap fungsi, yaitu
                - path('xml/', show_xml, name='show_xml'), untuk fungsi menampilkan semua dengan format XML
                - path('json/', show_json, name='show_json'), untuk fungsi menampilkan semua dengan format JSON
                - path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'), untuk fungsi menampilkan sesuai id dengan format XML
                - path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),untuk fungsi menampilkan sesuai id dengan format JSON
            </li>
            <li>
            Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman   
            form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
            Pertama buatlah di dalam block <a> sebuah button add product yang memindahkan ke url create_product.html. Dibawahnya buat sebuah blok if jika di dalam product_list masih
            kosong. Dibawahnya, di dalam blok else dari if sebelumnya, buat blok looping untuk semua produk yang sudah dibuat. Untuk setiap produknya, pertama tampilkan nama produknya dan hubungkan juga ke product_detail.html. Dibawahnya tampilkan thumbnail juga jika produk memilikinya. Terakhir tambahkan tombol more yang juga dihubungkan ke product_detail.html
            </li>
            <li>
            Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
            Di dalam blok template base.html, buat sebuah form dengan method POST. Buat table setelahnya berdasarkan atribut-atribut dari product. Terakhir tambahkan input yang menambah produk ke product_list.
            </li>
            <li>
            Membuat halaman yang menampilkan detail dari setiap data objek model.
            Di dalam blok template base.html, pertama buat button back to product list yang mengembalikan ke halaman utama. Dibawahnya tampilkan product_name dan atribut-atribut lainnya, seperti jika dia is_featured, price, rating, brand, dan juga kapan produknya ditambahkan. Dibawahnya tampilkan juga thumbnail, jika produk memilikinya. Terakhir buat blok paragraf untuk menyimpan product.description
            </li>
            <li>
            Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan sebelumnya?
            Kalau dari saya, tidak ada, karena dari web tutorial nya sudah sangat jelas dari step-by-step nya, lalu asisten dosennya pun selalu ada buat ngebantu kita kalo ada yang bermasalah.
            </li>
        </ol>
    </li>
    <li>
    Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
    <img src="images/postman_json_id.png" alt="Foto" width="1000">
    <img src="images/postman_json.png" alt="Foto" width="1000">
    <img src="images/postman_xml_id.png" alt="Foto" width="1000">
    <img src="images/postman_xml.png" alt="Foto" width="1000">
    </li>
</ol>

</details>

<details>
<Summary><b>Tugas 4</b></Summary>

<ol>
<li>
Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan dari Django yang digunakan untuk menangani proses autentikasi pengguna, seperti login. Form ini menyediakan validasi standar untuk username dan password, serta metode untuk memeriksa kredensial pengguna terhadap database.
Form ini terhubung dengan django sehingga langsung bisa dipakai untuk:
    <ol>
        <li>Menerima username dan password dari pengguna</li>
        <li>Memverifikasi kredensial ke database</li>
        <li>Memastikan akun yang dimasukkan aktif dan valid</li>
    </ol>
Kelebihan:
    <ol>
        <li>Mudah digunakan: Form ini sudah siap pakai, sehingga developer tidak perlu membuat form login dari awal.</li>
        <li>Integrasi dengan sistem autentikasi Django: Form ini bekerja mulus dengan sistem autentikasi bawaan Django, termasuk session dan middleware.</li>
        <li>Keamanan: Form ini sudah memiliki validasi dasar untuk mencegah serangan umum seperti brute force dan SQL injection.</li>
        <li>Dukungan untuk berbagai backend autentikasi: Form ini dapat digunakan dengan berbagai backend autentikasi yang didukung oleh Django.</li>
    </ol>
Kekurangan:
    <ol>
        <li>Keterbatasan kustomisasi: Form ini memiliki struktur dan validasi yang sudah ditentukan, sehingga sulit untuk menyesuaikan dengan kebutuhan spesifik aplikasi.</li>
        <li>Tidak mendukung fitur tambahan: Form ini hanya menangani login dasar, sehingga jika aplikasi membutuhkan fitur tambahan seperti two-factor authentication atau social login, developer harus menambahkannya secara manual.</li>
        <li>Tidak fleksibel untuk desain UI: Form ini memiliki tampilan standar yang mungkin tidak sesuai dengan desain UI aplikasi, sehingga perlu penyesuaian tambahan.</li>
    </ol>
</li>
<li>
Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi diibaratkan seperti apakah user ini benar-benar merupakan user yang diklaim orang tersebut. Biasanya prosesnya menggunakan username, password, token email, dll. Jika sudah dipastikan kalau orang tersebut merupakan user yang sesuai, maka sistem akan mengenalinya sebagai objek user
Sedangkan, otorisasi diibaratkan seperti apakah user ini boleh melakukan hal tertentu ini setelah dikenali. Proses otorisasi berarti menentukan hak akses hak akses (permissions) pengguna terhadap resource (misalnya view, model, atau data tertentu).
Django mengimplementasikan konsep autentikasi dengan menyediakan sistem authentication pada django.contrib.auth. Komponen dari sistem ini, yaitu
    <ol>
        <li>django.contrib.auth.authenticate() → memeriksa username/password dan mengembalikan User jika valid.</li>
        <li>django.contrib.auth.login() → menyimpan ID user di session sehingga user dianggap authenticated.</li>
        <li>Middleware: AuthenticationMiddleware → mengaitkan request.user dengan user yang sedang login.</li>
    </ol>
Sementara itu, Django mengimplementasikan konsep otorisasi salah satunya dengan decorators seperti @login_required dan @permission_required. Decorator ini bisa ditambahkan pada views untuk membatasi akses hanya untuk user yang sudah login atau memiliki permission tertentu. Selain itu, Django juga menyediakan model Group dan Permission untuk mengelola hak akses secara lebih terstruktur. 
</li>
<li>
Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Kelebihan dan kekurangan session:
    <ol>
        <li>Kelebihan:
            <ol>
                <li>Keamanan: Data session disimpan di server, sehingga lebih aman dari manipulasi oleh pengguna.</li>
                <li>Ukuran data: Session dapat menyimpan data yang lebih besar dibanding cookies karena tidak ada batasan ukuran seperti pada cookies.</li>
                <li>Meningkatkan pengalaman pengguna: Session memungkinkan penyimpanan informasi pengguna yang lebih kompleks, seperti keranjang belanja, tanpa membebani v.</li>
            </ol>
        </li>
        <li>Kekurangan:
            <ol>
                <li>Skalabilitas: Menggunakan session dapat menjadi tantangan pada aplikasi yang sangat besar atau terdistribusi karena perlu menyimpan state di server.</li>
                <li>Ketergantungan pada server: Jika server down, semua session akan hilang.</li>
                <li>Overhead server: Menyimpan dan mengelola session memerlukan sumber daya tambahan di server.</li>
            </ol>
        </li>
    </ol>
Kelebihan dan kekurangan cookies:
    <ol>
        <li>Kelebihan:
            <ol>
                <li>Skalabilitas: Cookies disimpan di klien, sehingga tidak membebani server dan lebih mudah untuk aplikasi yang sangat besar.</li>
                <li>Mudah diimplementasikan: Cookies mudah dibuat dan digunakan tanpa perlu konfigurasi server tambahan.</li>
                <li>Persistensi: Cookies dapat disetel untuk bertahan lebih lama, memungkinkan pengguna tetap login atau menyimpan preferensi meskipun browser ditutup.</li>
            </ol>
        </li>
        <li>Kekurangan:
            <ol>
                <li>Keamanan: Cookies rentan terhadap serangan seperti XSS dan CSRF karena data disimpan di klien dan dapat dimanipulasi.</li>
                <li>Batasan ukuran: Cookies memiliki batasan ukuran (sekitar 4KB), sehingga tidak cocok untuk menyimpan data besar.</li>
                <li>Privasi: Pengguna mungkin menonaktifkan cookies di browser mereka, yang dapat mengganggu fungsionalitas aplikasi web.</li>
            </ol>
        </li>
    </ol>
</li>
<li>
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default, penggunaan cookies tidak sepenuhnya aman dalam pengembangan web karena ada beberapa risiko potensial yang harus diwaspadai, seperti:
    <ol>
        <li>Serangan Cross-Site Scripting (XSS): Jika situs rentan terhadap XSS, penyerang dapat menyisipkan skrip berbahaya yang mencuri cookies pengguna.</li>
        <li>Serangan Cross-Site Request Forgery (CSRF): Cookies dapat digunakan untuk mengautentikasi permintaan, sehingga penyerang dapat memanfaatkan cookies yang valid untuk melakukan tindakan atas nama pengguna tanpa sepengetahuan mereka.</li>
        <li>Pencurian cookies: Jika cookies tidak dienkripsi atau dilindungi dengan benar, mereka dapat dicuri melalui jaringan yang tidak aman.</li>
        <li>Pengaturan yang salah: Cookies yang tidak dikonfigurasi dengan benar (misalnya, tidak menggunakan atribut Secure atau HttpOnly) dapat meningkatkan risiko keamanan.</li>
    </ol>
Django menangani risiko-risiko tersebut dengan beberapa cara:
    <ol>
        <li>CSRF Protection: Django memiliki perlindungan CSRF bawaan yang menggunakan token CSRF untuk memverifikasi bahwa permintaan POST berasal dari sumber yang sah.</li>
        <li>Secure and HttpOnly Flags: Django memungkinkan pengaturan atribut Secure (hanya dikirim melalui HTTPS) dan HttpOnly (tidak dapat diakses melalui JavaScript) pada cookies sesi untuk meningkatkan keamanan.</li>
        <li>Session Management: Django menggunakan session yang disimpan di server, sehingga data sensitif tidak disimpan langsung di cookies.</li>
        <li>Input Validation: Django menyediakan mekanisme validasi input yang membantu mencegah serangan XSS dengan membersihkan data yang diterima dari pengguna.</li>
        <li>Pengaturan Kebijakan Keamanan Konten (CSP): Django mendukung pengaturan CSP untuk membatasi sumber daya yang dapat dimuat oleh halaman web, mengurangi risiko XSS.</li>
    </ol>
</li>   
<li>
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    <ol>
        <li>Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
        Pertama, buat fungsi untuk registrasi, login, dan logout di views.py. Untuk fungsi registrasi dibuat menggunakan request method POST dan form bawaan django, yaitu  UserCreationForm() yang jika form berhasil diisi (valid) dipindahkan ke laman login. Untuk fungsi login juga menggunakan request method POST dan form bawaan django, yaitu AuthenticationForm(). Jika sudah berhasil mengisi form akan dipindahkan ke laman login. Untuk logout, tinggal tambahkan fungsi bawaan django, yaitu logout() dan pindahkan ke laman login. Setelah dibuat semua fungsi, buat juga laman html nya untuk menampilkan fungsi tersebut kecuali logout yang hanya menambahkan tombol logout pada main.html yang mengarahkan ke laman login. Untuk htmlnya, yaitu login dan register, pertama-tama extend base.html. Lalu, di dalam block content buat form dengan method POST. Tambahkan juga csrf_token di dalam form. Setelah itu, buat table yang berisi input sesuai dengan atribut yang dibutuhkan pada form. Terakhir, tambahkan tombol submit untuk mengirim form tersebut. Terakhir, buat routing di urls.py untuk setiap fungsi yang sudah dibuat.
        </li>
        <li>Menghubungkan model Product dengan User
        Pertama, import User dari django.contrib.auth.models di models.py. Setelah itu, tambahkan atribut baru pada class Product dengan nama 'user' yang bertipe ForeignKey dan menghubungkannya ke model User dengan on_delete=models.CASCADE. Setelah itu, jalankan perintah makemigrations dan migrate untuk menerapkan perubahan pada database. Lalu, pada views.py di fungsi create_product, tambahkan parameter commit=False di product_entry agar product yang terbuat tidak langsung masuk ke database, tambahkan juga parameter request_user ke atribut user pada product_entry, lalu simpan product_entry ke database dengan product_entry.save(). Terakhir, tambahkan juga atribut user pada context di fungsi show_main agar bisa ditampilkan di main.html
        </li>
        <li> Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
        Pertama, pada views.py di fungsi show_main, tambahkan parameter request.user.username pada 'name' ke context agar bisa menampilkan username di main.html. Tambahkan juga request.COOKIES.get('last_login', 'Never') ke context 'last_login' untuk menampilkan waktu terakhir login. Agar bisa menyimpan waktu terakhir login pada cookies, tambahkan response.set_cookie('last_login', str(datetime.datetime.now())) pada fungsi login_user yang berfungsi untuk mendaftarkan cookie last_login di response dengan isi timestamp terkini. Setelah itu, pada main.html, tambahkan juga paragraf yang menampilkan last_login dari cookies. Terakhir, pada fungsi logout_user, tambahkan response.delete_cookie('last_login') untuk menghapus cookies last_login ketika user logout.
        </li>
    </ol>
</li>
</ol>
<img src="images/produk_akun1.png" alt="Foto" width="1000">
<img src="images/produk_akun2.png" alt="Foto" width="1000">
</details>