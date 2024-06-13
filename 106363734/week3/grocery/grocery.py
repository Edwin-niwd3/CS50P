itemList = {}
while True:
    try:
        item = input()
        item = item.lower()
        if item in itemList:
            itemList[item] += 1
        else:
            itemList.__setitem__(item, 1)
    except EOFError:
        for item in sorted(itemList):
            print(itemList[item], item.upper())
        break
