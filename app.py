# 1. Impor kelas Flask dari pustaka flask
from flask import Flask

# 2. Buat sebuah instance dari aplikasi web Flask
#    __name__ adalah variabel khusus Python yang memberikan nama modul saat ini.
app = Flask(__name__)

# 3. Definisikan sebuah "route" atau rute.
#    Decorator @app.route('/') memberitahu Flask URL mana yang harus memicu fungsi kita.
#    '/' adalah rute dasar (halaman utama).
@app.route('/')
def hello_world():
    # 4. Fungsi ini akan dijalankan ketika seseorang mengunjungi rute '/'
    #    dan akan mengembalikan teks "Hello, World!" ke browser.
    return 'Hello, World!'

# 5. Blok ini memastikan server hanya berjalan jika skrip ini dieksekusi secara langsung.
#    Ini diperlukan agar server tidak berjalan jika file ini diimpor ke file lain.
if __name__ == '__main__':
    # Menjalankan aplikasi pada server pengembangan lokal.
    # debug=True akan secara otomatis me-restart server setiap kali Anda menyimpan perubahan kode.
    app.run(debug=True)