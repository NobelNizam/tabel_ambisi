import csv
from rich.console import Console
from rich.table import Table
import os; import time
from alive_progress import alive_bar

rows = [
    ["1", "NA", "NA", "NA"],
    ["2", "NA", "NA", "NA"],
    ["3", "NA", "NA", "NA"],
    ["4", "NA", "NA", "NA"],
    ["5", "NA", "NA", "NA"],
    ["6", "NA", "NA", "NA"],
]

# fungsi untuk memuat data template dari rows
def tabel():
    table = Table(title="\nTabel Ambisi")
    columns = ["Semester", "Tujuan", "Kenyataan", "Usaha"]
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='bright_green')
    console = Console()
    console.print(table)

# fungsi untuk menjalanankan opsi edit tabel
def editData():
    smester = input('Pilih Semester -> ')
    if smester in [row[0] for row in rows[0:]]:
        print(f"Anda memasuki semester {smester}")
        index = int(smester)-1
        tujuan = input("Masukan Tujuan Baru -> ")
        kenyataan = input("Masukan Kenyataan Baru -> ")
        usaha = input("Masukan Usaha Baru -> ")
        rows[index][1] = tujuan
        rows[index][2] = kenyataan
        rows[index][3] = usaha
        print("Data Telah Update!")
    else:
        print(f"Tidak ada semester {smester} tersebut!") 

# fungsi menyimpan data yang telah di edit ke dalam file csv
def simpanData():
    with alive_bar(100, title='Menyimpan data..') as bar:
        with open('D:/Proyek/dataTabelAmbisi.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            for _ in range(100):
                time.sleep(.02)
                bar()
    print("Data berhasil disimpan.")

# fungsi memuat data yang telah disimpan sebelumnya
def muatData():
    global rows
    try:
        with alive_bar(100, title='Memuat data..') as bar:
            with open('D:/Proyek/dataTabelAmbisi.csv', mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                for _ in range(100):
                    time.sleep(.05)
                    bar()
        print("Data berhasil dimuat.")
    except FileNotFoundError:
        print("Tidak ada file tersebut.")


# fungsi looping untuk menjalankan fungsi tabel disertai menu
def main():
    while True:
        tabel()
        print('\nMenu:')
        print("1 -> Ubah Ambisi")
        print("2 -> Simpan Data")
        print("3 -> Muat Data")
        print("4 -> Keluar\n")
        pilihan = input("Pilih opsi -> ")
        if pilihan == "1":
            editData()
        elif pilihan == "2":
            simpanData()
        elif pilihan == "3":
            muatData()
        elif pilihan == "4":
            print("Keluar dari program.")
            os.system('cls')
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()