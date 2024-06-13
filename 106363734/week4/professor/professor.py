import random

def main():
    level = get_level()
    game_counter = 1
    attempts_counter = 0
    correct_counter = 0
    while game_counter <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x+y
        while attempts_counter != 3:
            print(x, "+" , y , "=")
            try:
                answer = int(input())
                if answer == correct:
                    correct_counter+=1
                    break
                else:
                    attempts_counter+=1
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
        if attempts_counter == 3:
            print(x, "+", y, "=", correct)
        attempts_counter = 0
        game_counter+=1
    #when we exit the look, we are done with questions, so print score
    print(correct_counter)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        return x
    elif level == 2:
        x = random.randint(10,99)
        return x
    elif level == 3:
        x = random.randint(100,999)
        return x

if __name__ == "__main__":
    main()
