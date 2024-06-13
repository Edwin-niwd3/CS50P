

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    Signal = gauge(percentage)
    print(Signal)

def convert(fraction):
        x,y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        percentage = round(x/y * 100)
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
