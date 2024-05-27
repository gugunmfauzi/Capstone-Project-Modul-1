# Data Siswa
data_siswa = [
    {
        "Nama": "Hendra",
        "NIM": "001",
        "Gender": "Pria",
        "Alamat": "Jalan Sukajadi",
        "Nilai": 90
    },
    {
        "Nama": "Aulia",
        "NIM": "002",
        "Gender": "Wanita",
        "Alamat": "Jalan Sukamanah",
        "Nilai": 70
    },
    {
        "Nama": "Amin",
        "NIM": "003",
        "Gender": "Pria",
        "Alamat": "Jalan Asia Afrika",
        "Nilai": 60
    },
    {
        "Nama": "Hasan",
        "NIM": "004",
        "Gender": "Pria",
        "Alamat": "Jalan Cipaganti",
        "Nilai": 80
    },
    {
        "Nama": "Selvi",
        "NIM": "005",
        "Gender": "Wanita",
        "Alamat": "Jalan Anggrek",
        "Nilai": 85
    }
]

# Fungsi untuk menampilkan data siswa
def read_siswa():
    print("Menampilkan Data Siswa")
    if not data_siswa:
        print("Tidak ada data siswa.\n")
        return

    print("{:<5} | {:<15} | {:<10} | {:<20} | {:<5} | {:<15}".format("NIM", "Nama", "Gender", "Alamat", "Nilai", "Grade"))
    print("-" * 80)
    for siswa in data_siswa:
        grade = calculate_grade(siswa['Nilai'])
        print("{:<5} | {:<15} | {:<10} | {:<20} | {:<5} | {:<15}".format(siswa['NIM'], siswa['Nama'], siswa['Gender'], siswa['Alamat'], siswa['Nilai'], grade))
    print()

# Fungsi untuk menambahkan data siswa
def create_siswa():
    print("Menambahkan Data Siswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    gender = input("Gender(Pria/Wanita): ")
    alamat = input("Alamat: ")
    
    while True:
        nilai = int(input("Nilai: "))
        if 0 <= nilai <= 100:
            break
        else:
            print("Nilai harus antara 0 dan 100.")

    data_siswa.append({"Nama": nama, "NIM": nim, "Gender": gender, "Alamat": alamat, "Nilai": nilai})
    print("Data siswa berhasil ditambahkan!\n")

# Fungsi untuk mengubah data siswa
def update_siswa():
    print("Mengubah Data Siswa")
    
    attempts = 0
    while attempts < 5:
        nim = input("Masukkan NIM siswa yang akan diubah: ")
        siswa = next((s for s in data_siswa if s['NIM'] == nim), None)
        if siswa:
            break
        else:
            print("NIM tidak ditemukan, silakan masukkan NIM yang valid.")
            attempts += 1
    else:
        print("Percobaan lebih dari 5 kali. Kembali ke menu utama.\n")
        return
    
    print(f"Data saat ini - Nama: {siswa['Nama']}, Gender: {siswa['Gender']}, Alamat: {siswa['Alamat']}, Nilai: {siswa['Nilai']}")
    siswa['Nama'] = input("Nama: ")
    siswa['Gender'] = input("Gender(Pria/Wanita): ")
    siswa['Alamat'] = input("Alamat: ")

    while True:
        nilai = int(input("Nilai: "))
        if 0 <= nilai <= 100:
            siswa['Nilai'] = nilai
            break
        else:
            print("Nilai harus antara 0 dan 100.")

    print("Data siswa berhasil diubah!\n")

# Fungsi untuk menghapus data siswa
def delete_siswa():
    print("Menghapus Data Siswa")
    
    attempts = 0
    while attempts < 5:
        nim = input("Masukkan NIM siswa yang akan dihapus: ")
        siswa = next((s for s in data_siswa if s['NIM'] == nim), None)
        if siswa:
            data_siswa.remove(siswa)
            print("Data siswa berhasil dihapus!\n")
            return
        else:
            print("NIM tidak ditemukan, silakan masukkan NIM yang valid.")
            attempts += 1
    else:
        print("Percobaan lebih dari 5 kali. Kembali ke menu utama.\n")


# Fungsi untuk menghitung grade
def calculate_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 85:
        return "A-"
    elif nilai >= 80:
        return "B"
    elif nilai >= 75:
        return "B-"
    elif nilai >= 70:
        return "C"
    elif nilai >= 65:
        return "D"
    elif nilai > 40:
        return "Perlu Remedial"
    else:
        return "Tidak Lulus"

# Menu utama
def main_menu():
    while True:
        pilihan_menu = input('''
Selamat Datang di Aplikasi Data Nilai Siswa SMAN 5 Bandung
        
Main Menu :
1. Menampilkan Data Siswa
2. Menambahkan Data Siswa
3. Mengubah Data Siswa
4. Menghapus Data Siswa
5. Keluar Aplikasi
        
Masukkan angka Menu yang akan dipilih: ''')

        if pilihan_menu == "1":
            read_siswa()
        elif pilihan_menu == "2":
            create_siswa()
        elif pilihan_menu == "3":
            update_siswa()
        elif pilihan_menu == "4":
            delete_siswa()
        elif pilihan_menu == "5":
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan menu utama
main_menu()
