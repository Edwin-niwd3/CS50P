while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise Exception
        percentage = int(round(x/y * 100))
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except Exception:
        pass


if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(str(percentage) + "%")
