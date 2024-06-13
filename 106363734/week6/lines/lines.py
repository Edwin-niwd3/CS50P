import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if check_suffix(sys.argv[1]):
        print(line_counter(sys.argv[1]))
    else:
        sys.exit("Not a Python file")

def check_suffix(name):
    suffix = name.split(".")
    return suffix[1].startswith("py")

def line_counter(name):
    line_counter = 0
    try:
        with open(name, "r") as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") or line.strip() == "":
                    pass
                else:
                    line_counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return line_counter


if __name__ == "__main__":
    main()
