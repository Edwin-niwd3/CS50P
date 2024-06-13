
def shorten(word):
    answer = ""
    for letter in word:
        if letter.upper() != "A" and letter.upper() != "E" and letter.upper() != "I" and letter.upper() != "O" and letter.upper() != "U":
            answer += letter
    return answer

def main():
    answer = ''
    sentence = input("Input: ")
    answer = shorten(sentence)
    print(answer)


if __name__ == "__main__":
    main()
