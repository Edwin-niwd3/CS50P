
def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.strip()
    #check to make sure it is not hello and does not include hello
    if greeting.find("hello") != -1:
        return 0
    #Check if the first letter is h
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print("$",val, sep = "")

if __name__ == "__main__":
    main()
