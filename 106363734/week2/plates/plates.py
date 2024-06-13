def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #Basic checks that can be done out of a loop
    if 2 > len(s) or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    #Flag needed outside
    numberFlag = False
    for letter in s:
        if letter.isdigit():
            #if it's the first number we come across and it is 0, return false
            if numberFlag == False and letter == '0':
                return False
            else:
                #else we can set the numberFlag to true for later purposes
                numberFlag = True
        #at this point, we know it's not a digit, so we can check to make sure it is at least an actual letter
        elif not letter.isalpha():
            return False
            #if not, then we can assume it's not a letter or digit, therefore return false
        #if we continue, we know it is a letter
        elif letter.isalpha() and numberFlag:
            return False
            #this is only true if we have seen a digit before and yet we see another letter, which means that the number is not at the end of the plate
    return True
    #if we get through all the checks then it is a legal plate
main()
