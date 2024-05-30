# Membuat fungsi untuk memvalidasi input
def validate_input(input_data):
    if input_data.strip() == '':
        return False
    return True

# Membuat fungsi untuk memproses pendaftaran
def process_registration(nim, nama, asal):
    if validate_input(nim) and validate_input(nama) and validate_input(asal):
        # Lakukan proses pendaftaran di sini
        print("Pendaftaran berhasil!")
    else:
        print("Mohon lengkapi semua data pendaftaran.")

# Meminta input dari pengguna
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")
asal = input("Masukkan Asal: ")

# Memproses pendaftaran
process_registration(nim, nama, asal)
