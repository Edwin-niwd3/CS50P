import sys
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line")
    #read everything in the first file
    students_dictionary = read_files(sys.argv[1])
    #fix the information to be in first, last, house format
    fixed_dictionary = fix_info(students_dictionary)
    insert_info(fixed_dictionary, sys.argv[2])

def read_files(file_1):
    students_info = []
    try:
        with open(file_1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_info.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Couldn't open file")
    return students_info

def fix_info(dictionary):
    fixed_info = []
    for student in dictionary:
        #split apart the names
        last,first  = student["name"].split(",")
        first = first.strip()
        last = last.strip()
        fixed_info.append({"first": first, "last" : last, "house": student["house"]})
    return fixed_info

def insert_info(dictionary, file_2):
    with open(file_2, 'w') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        for student in dictionary:
            writer.writerow(student)
if __name__ == "__main__":
    main()
