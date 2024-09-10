import csv
from rich.console import Console
from rich.table import Table
import os
import time
from alive_progress import alive_bar

# Menentukan directory penyimpanan data
direktori_sekarang = os.getcwd()
filename = os.path.join(direktori_sekarang, "data_tabel.csv")

rows = [
    ["1", "NA", "NA", "NA"],
    ["2", "NA", "NA", "NA"],
    ["3", "NA", "NA", "NA"],
    ["4", "NA", "NA", "NA"],
    ["5", "NA", "NA", "NA"],
    ["6", "NA", "NA", "NA"],
]

console = Console()

# fungsi untuk memuat data template dari rows
def tabel():
    table = Table(title="\nTabel Ambisi", title_justify="center", show_header=True, header_style="bold magenta", border_style="bright_blue")
    columns = ["Semester", "Tujuan", "Kenyataan", "Usaha"]
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='bright_green')
    console.print(table)
    console.print("\nTotal Semester yang dimasukkan: {}".format(len(rows)), style="bold green")

# fungsi untuk menjalanankan opsi edit tabel dengan progress bar
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

# fungsi menyimpan data yang telah di edit ke dalam file csv dengan progress bar
def simpanData():
    with alive_bar(100, title='Menyimpan data...') as bar:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            for _ in range(100):
                time.sleep(.02)
                bar()
    print("Data berhasil disimpan.")

# fungsi memuat data yang telah disimpan sebelumnya dengan progress bar
def muatData():
    global rows
    try:
        with alive_bar(100, title='Memuat data...') as bar:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                for _ in range(100):
                    time.sleep(.03)
                    bar()
        print("Data berhasil dimuat.")
    except FileNotFoundError:
        print("Tidak ada file tersebut.")

# fungsi looping untuk menjalankan fungsi tabel disertai menu
def main():
    while True:
        tabel()
        console.print('\nMenu:', style="bold green")
        console.print("1 -> Ubah Ambisi", style="bold green")
        console.print("2 -> Simpan Data", style="bold green")
        console.print("3 -> Muat Data", style="bold green")
        console.print("4 -> Keluar\n", style="bold green")
        
        pilihan = input("Pilih opsi -> ")
        
        if pilihan == "1":
            editData()
        elif pilihan == "2":
            simpanData()
        elif pilihan == "3":
            muatData()
        elif pilihan == "4":
            console.print("Keluar dari program.", style="bold red")
            time.sleep(1)
            os.system('cls')
            break
        else:
            console.print("Opsi tidak valid. Silakan coba lagi.", style="bold red")

if __name__ == "__main__":
    main()
