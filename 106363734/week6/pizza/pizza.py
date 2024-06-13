import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too little arguments")
    if check_name(sys.argv[1]):
        menu = readFile(sys.argv[1])
    else:
        sys.exit("File does not exist")
    displayMenu(menu)

def check_name(name):
    suffix = name.split(".")
    return suffix[1].startswith("csv")

def readFile(name):
    try:
        with open(name) as file:
            reader = csv.reader(file)
            menu = tabulate(reader, headers = "firstrow", tablefmt = "grid")
            return menu
    except FileNotFoundError:
        sys.exit("File does not exist")

def displayMenu(menu):
    print(menu)

if __name__ == "__main__":
    main()
