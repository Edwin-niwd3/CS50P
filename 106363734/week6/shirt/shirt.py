import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    check_files(sys.argv[1], sys.argv[2])
    transpose_images(sys.argv[1], sys.argv[2])

def check_files(file_1, file_2):
    valid = ["png", "jpg", "jpeg"]
    name1, type1 = file_1.split(".")
    name2, type2 = file_2.split(".")
    if not type1 in valid:
        sys.exit("Invalid input")
    elif not type2 in valid:
        sys.exit("Invalid input")
    elif type1 != type2:
        sys.exit("Input and output have different extensions")

def transpose_images(file_1, file_2):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(file_1) as photo:
            cropped = ImageOps.fit(photo, shirt.size)
            cropped.paste(shirt, mask = shirt)
            cropped.save(file_2)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
