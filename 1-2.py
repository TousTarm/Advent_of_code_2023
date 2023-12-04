with open('input1.txt',newline="\n") as file:
    line = file.readlines()

word = "76xkqjzqtwonfour"

result = []
number = []
words = ["one","two","three","four","five","six","seven","eight","nine"]

for index,strword in enumerate(words):
    temp = word.find(strword)
    tempnum = ""
    if(temp != -1):
        print(int(index+1))

"""
for ln in range(len(word)):
    if(word[ln].isdigit()):
        number += str(word[ln])
    for tempn in range(len(temp)):
        if(ln == temp[tempn]):
            tempnumber = temp[tempn] #tempnumber = index pismena ze stringu
            tempnum = ""
            for a in range(len(words)):
                tempnum = word[int(tempnumber)]
            print(tempnum)
total = 0
for i in range(len(result)):
    total += int(result[i])
print(total)
"""