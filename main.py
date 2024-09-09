from rich.console import Console
from rich.table import Table

def tabel():
    table = Table(title="\nTabel Ambisi")
    rows = [
        ["1", "NA", "NA", "NA"],
        ["2", "NA", "NA", "NA"],
        ["3", "NA", "NA", "NA"],
        ["4", "NA", "NA", "NA"],
        ["5", "NA", "NA", "NA"],
        ["6", "NA", "NA", "NA"],
    ]
    columns = ["Semester", "Tujuan", "Kenyataan", "Usaha"]
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*row, style='bright_green')
    console = Console()
    console.print(table)
opsi = ['1', '2', '3', '4', '5', '6']
def editData():
    smester = input('Pilih Semester -> ')
    if smester in opsi:
        print(f"Anda memasuki semester {smester}")
    elif smester not in opsi:
        print(f"Tidak ada semester {smester} tersebut!") 

def main():
    while True:
        tabel()
        print("1 - Edit")
        print("2 - Exit")
        pilihan = input("Pilih opsi (1/2): ")
        if pilihan == "1":
            print("tesss")
            editData()
        elif pilihan == "2":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()