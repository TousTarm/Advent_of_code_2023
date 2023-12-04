word = "76xkqjzqtwonfour"

result = []
number = []
words = ["one","two","three","four","five","six","seven","eight","nine"]
temp = []

result.append(None)
number.append("")
for index,x in enumerate(words):
    temp = word.find(x)
    tempnum = ""
    if(temp != -1):
        for y in range(len(x)):
            tempnum += word[temp+y]
        print(tempnum)