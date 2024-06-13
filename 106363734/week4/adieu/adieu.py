import inflect
import sys

engine = inflect.engine()
nameList = []

while True:
    try:
        #first we save all the names we need
        name = input()
        nameList.append(name)
    except EOFError:
        new_list = engine.join(nameList)
        break
print("Adieu, adieu, to " + new_list)
