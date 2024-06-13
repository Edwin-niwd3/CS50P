answer = ''
camelCase = input("camelCase: " )
for index in range(len(camelCase)):
    if camelCase[index].isupper():
        answer += '_' + camelCase[index].lower()
    else:
        answer += camelCase[index]
print("snake_case:", answer)
