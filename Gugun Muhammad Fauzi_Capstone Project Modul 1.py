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

# Fungsi untuk menambahkan data siswa
def create_siswa():
    print("Menambahkan Data Siswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    gender = input("Gender: ")
    alamat = input("Alamat: ")
    nilai = int(input("Nilai: "))

    if nilai > 100:
        print("Nilai yg anda Masukkan diLuar Jangkauan\n")
    elif nilai < 0:
        print("Tidak menerima Nilai Negatif\n")
    else:
        siswa = {
            "Nama": nama,
            "NIM": nim,
            "Gender": gender,
            "Alamat": alamat,
            "Nilai": nilai
        }
        data_siswa.append(siswa)
        print("Data siswa berhasil ditambahkan!\n")

# Fungsi untuk menampilkan data siswa
def read_siswa():
    print("Menampilkan Data Siswa")
    if len(data_siswa) == 0:
        print("Tidak ada data siswa.\n")
    else:
        print("{:<5} | {:<15} | {:<10} | {:<20} | {:<5} | {:<15}".format("NIM", "Nama", "Gender", "Alamat", "Nilai", "Grade"))
        print("-" * 80)
        for siswa in data_siswa:
            grade = calculate_grade(siswa['Nilai'])
            print("{:<5} | {:<15} | {:<10} | {:<20} | {:<5} | {:<15}".format(siswa['NIM'], siswa['Nama'], siswa['Gender'], siswa['Alamat'], siswa['Nilai'], grade))
        print()

# Fungsi untuk mengubah data siswa
def update_siswa():
    print("Mengubah Data Siswa")
    nim = input("Masukkan NIM siswa yang akan diubah: ")
    found = False
    for siswa in data_siswa:
        if siswa['NIM'] == nim:
            found = True
            print(f"Data saat ini - Nama: {siswa['Nama']}, Gender: {siswa['Gender']}, Alamat: {siswa['Alamat']}, Nilai: {siswa['Nilai']}")
            siswa['Nama'] = input("Nama baru: ")
            siswa['Gender'] = input("Gender baru: ")
            siswa['Alamat'] = input("Alamat baru: ")
            nilai = int(input("Nilai baru: "))

            if nilai > 100:
                print("Nilai yg anda Masukkan diLuar Jangkauan\n")
            elif nilai < 0:
                print("Tidak menerima Nilai Negatif\n")
            else:
                siswa['Nilai'] = nilai
                print("Data siswa berhasil diubah!\n")
            break
    if not found:
        print("Data siswa tidak ditemukan.\n")

# Fungsi untuk menghapus data siswa
def delete_siswa():
    print("Menghapus Data Siswa")
    nim = input("Masukkan NIM siswa yang akan dihapus: ")
    found = False
    for siswa in data_siswa:
        if siswa['NIM'] == nim:
            found = True
            data_siswa.remove(siswa)
            print("Data siswa berhasil dihapus!\n")
            break
    if not found:
        print("Data siswa tidak ditemukan.\n")

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
        PilihanMenu = input('''
Selamat Datang di Aplikasi Data Siswa SMAN 5 Bandung
        
Main Menu :
1. Menambahkan Data Siswa
2. Menampilkan Data Siswa
3. Mengubah Data Siswa
4. Menghapus Data Siswa
5. Keluar dari program
        
Masukan angka Menu yang akan dipilih : ''')

        if PilihanMenu == "1":
            create_siswa()
        elif PilihanMenu == "2":
            read_siswa()
        elif PilihanMenu == "3":
            update_siswa()
        elif PilihanMenu == "4":
            delete_siswa()
        elif PilihanMenu == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan menu utama
main_menu()
