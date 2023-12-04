word = "76xkqjzqtwonfour"

result = []
words = ["one","two","three","four","five","six","seven","eight","nine"]
temp = []
for index,x in enumerate(words):
    tnumber = word.find(x)
    if(tnumber != -1):
        temp.append(tnumber)
number = ""
for ln in range(len(word)):
    if(word[ln].isdigit()):
        number += str(word[ln])
    for tempn in range(len(temp)):
        if(ln == temp[tempn]):
            tempnumber = temp[tempn] #tempnumber = index pismena ze stringu
            tempnum = ""
            for index,strword in enumerate(words):
                tempw = word.find(strword)
                tempnum = ""
                if(tempw != -1):
                    print(int(index+1))

"""
result.append(None)
number.append("")
for index,x in enumerate(words):
    temp = line.find(x)
    tempnum = ""
    if(temp != -1):
        for y in range(len(x)):
            tempnum += line[temp+y]
        number += tempnum
print(number)
"""