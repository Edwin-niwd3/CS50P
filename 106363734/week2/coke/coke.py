dueAmount = 50
while dueAmount > 0:
    print("Amount Due:", dueAmount)
    inserted = int(input("Insert Coin: "))
    if inserted == 25 or inserted == 10 or inserted == 5:
        dueAmount -= inserted
#if we exit the while loop, then we know the dueAmount is either 0, or less than 0
#we can just multiply the dueAmount by -1 to get a positive number, so we can save on space
dueAmount *= -1
print("Change Owed:", dueAmount)
