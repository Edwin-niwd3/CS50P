greeting = input("Greeting: ")
greeting = greeting.lower()
greeting = greeting.strip()
#check to make sure it is not hello and does not include hello
if greeting.find("hello") != -1:
    print("$0")
#Check if the first letter is h
elif greeting[0] == 'h':
    print("$20")
else:
    print("$100")
