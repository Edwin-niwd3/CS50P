def checkVowel(letter):
    letter = letter.upper()
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        return True
    return False
def Main():
    answer = ''
    sentence = input("Input: ")
    for letter in sentence:
        if not checkVowel(letter):
            answer += letter
    print(answer)
Main()
