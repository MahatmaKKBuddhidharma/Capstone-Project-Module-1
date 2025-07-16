from tabulate import tabulate

# Daftar data dokter
data_dokter = [
    {'ID': '01', 'nama': 'Surya', 'password': 'qwerty', 'class': 'dokter'},
    {'ID': '02', 'nama': 'Ratna', 'password': '1234', 'class': 'admin'},
]

# Daftar data pasien 
daftar_pasien = [
    {"ID": "01", "Nama pasien": "Rian", "Diagnosa": "Hipertensi paru", "Fasilitas yang dipakai": "Ventilator"},
    {"ID": "02", "Nama pasien": "Sarjidno", "Diagnosa": "Gastroentritis", "Fasilitas yang dipakai": "IV infus"},
    {"ID": "03", "Nama pasien": "Imah", "Diagnosa": "UTI", "Fasilitas yang dipakai": "Dialisis"}
]

# Menampilkan Data (Read)
def tampilkan_data_pasien():
    print("\n=== Data Pasien ===")
    tabel_pasien = tabulate(daftar_pasien, headers="keys", tablefmt="grid")
    print(tabel_pasien)

# Menu Utama
def menu_utama(rclass):
    print("\n=== Menu Utama ===")
    print("1. Tampilkan data pasien")
    print("2. Tambahkan data pasien")
    print("3. Perbarui data pasien")
    if rclass == "admin":
        print("4. Hapus data pasien")
    print("5. Log Out")
    print("6. Exit")
    input_menu_utama(rclass)

# Menambahkan Data (Create)
def tambah_data(rclass):
    tampilkan_data_pasien()
    while True:
        inp_ID = input("Masukkan ID pasien baru: ")
        if any (pasien["ID"] == inp_ID for pasien in daftar_pasien):
            print(f"ID {inp_ID} sudah digunakan. Harap masukkan ID yang berbeda.")
        else:
            break
    inp_nama = input("Masukkan nama pasien baru: ")
    inp_diagnosa = input("Masukkan diagnosa pasien baru: ")
    inp_fasilitas = input("Masukkan fasilitas yang dipakai pasien baru: ")
    daftar_pasien.append({
    "ID": inp_ID,
    "Nama pasien": inp_nama,
    "Diagnosa": inp_diagnosa,
    "Fasilitas yang dipakai": inp_fasilitas
     })
    tampilkan_data_pasien()
    print("Data pasien baru berhasil dimasukkan!")
    menu_utama(rclass)

# Memperbarui Data (Update)
def update_data(rclass):
    tampilkan_data_pasien()
    update_pasien = input("Masukkan ID pasien: ")
    for pasien in daftar_pasien:
        if pasien["ID"] == update_pasien:
            print("ID ditemukan! Pilih data apa yang akan diperbarui:")
            print("1. Diagnosa")
            print("2. Fasilitas yang dipakai")
            pilih_update = input("Masukkan pilihan: ")
            if pilih_update == "1":
                pasien["Diagnosa"] = input("Masukkan diagnosa baru: ")
            elif pilih_update == "2":
                pasien["Fasilitas yang dipakai"] = input("Masukkan fasilitas baru: ")
            else:
                print("Pilihan tidak valid.")
                return
            print(f"ID {update_pasien} berhasil diperbarui.")
            tampilkan_data_pasien()
            menu_utama(rclass)
            return
    print("ID tidak ditemukan.")
    menu_utama(rclass)

# Menghapus Data (Delete)
def hapus_data(rclass):
    tampilkan_data_pasien()
    inp_hapus = input("Masukkan ID pasien yang akan dihapus: ")
    for pasien in daftar_pasien:
        if pasien["ID"] == inp_hapus:
            konfirmasi = input(f"Apakah anda yakin ingin menghapus data pasien dengan ID {inp_hapus}? (y/n): ").lower()
            if konfirmasi == 'y':
                daftar_pasien.remove(pasien)
                print(f"ID {inp_hapus} berhasil dihapus.")
                tampilkan_data_pasien()
            else:
                print("Penghapusan dibatalkan.")
            tampilkan_data_pasien()
            menu_utama(rclass)
            return
    print("ID tidak ditemukan.")
    menu_utama(rclass)

# Menangani input dari menu utama
def input_menu_utama(rclass):
    inp_pilihan = input("Masukkan menu yang akan dituju: ")
    if inp_pilihan == "1":
        tampilkan_data_pasien()
        menu_utama(rclass)
    elif inp_pilihan == "2":
        tambah_data(rclass)
    elif inp_pilihan == "3":
        update_data(rclass)
    elif inp_pilihan == "4":
        if rclass == "admin":
            hapus_data(rclass)
        else:
            print("Akses ditolak. Hanya admin yang dapat menghapus data pasien.")
            menu_utama(rclass)
    elif inp_pilihan == "5":
        login()
    elif inp_pilihan == "6":
        print("Mematikan program...")
        return
    else:
        print("Input tidak valid! Harap masukkan input yang valid!")
        menu_utama(rclass)


# Fungsi login berbasis role, dengan role tertera pada data dokter. Role terbagi menjadi dua, role dokter dan role admin
def login():
    ID_input = input("Masukkan ID Anda: ")
    pas_input = input("Masukkan password Anda: ")
    for id_class in data_dokter:
        if id_class['ID'] == ID_input and id_class['password'] == pas_input:
            print(f"\nSelamat datang, {id_class['class']} {id_class['nama']}")
            menu_utama(id_class["class"])
            return
    print("ID atau Password salah. Silakan coba lagi.")
    login()

#Mulai program. Merupakan fungsi yang berjalan ketika pertama kali dijalankan
login()