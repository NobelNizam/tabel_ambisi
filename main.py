from rich.console import Console
from rich.table import Table
# test 
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