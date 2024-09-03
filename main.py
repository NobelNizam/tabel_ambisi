from rich.console import Console
from rich.table import Table

table = Table(title="\nTabel Ambisi")
rows = [
    ["1", "Doe", "45", "NA"],
    ["2", "Doe", "45", "NA"],
    ["3", "Doe", "45", "NA"],
    ["4", "Doe", "45", "NA"],
    ["5", "Doe", "45", "NA"],
    ["6", "Doe", "45", "NA"],
]
columns = ["Semester", "Tujuan", "Kenyataan", "Usaha"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style='bright_green')

console = Console()
console.print(table)