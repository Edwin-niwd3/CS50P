def convert(time):
    #In the format of ##:##, I can split by using the :
    hours,minutes = time.split(':')
    #convert minutes
    minutes = float(minutes)
    minutes = minutes/60
    total_time = float(hours) + minutes
    return total_time

def main():
    time = input("What time is it? ")
    total_time = convert(time)
    if 7 <= total_time <= 8:
        print("breakfast time")
    elif 12 <= total_time <= 13:
        print("lunch time")
    elif 18 <= total_time <= 19:
        print("dinner time")
if __name__ == "__main__":
    main()
