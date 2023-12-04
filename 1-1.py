with open('input1-1.txt',newline="\n") as file:
    line = file.readlines()

result = []
number = []
for i in range(len(line)):
    word = line[i]
    result.append(None)
    number.append(None)
    for x in range(len(word)):
        if (word[x].isdigit()) and (result[i] is None):
            result[i] = int(word[x])*10
            number[i] = int(word[x])
        elif word[x].isdigit():
            number[i] = int(word[x])
    result[i] += number[i]

total = 0
for i in range(len(result)):
    total += int(result[i])
print(total)