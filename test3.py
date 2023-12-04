word = "76xkqjzqtwonfour"

words = ["one","two","three","four","five","six","seven","eight","nine"]

result = []
number = []
temp = []

result.append(None)
number.append("")
for wordnumber in range(len(word)):
    if(word[wordnumber].isdigit()):
        print(word[wordnumber])
    for index,x in enumerate(words):
        temp = word.find(x)
        tempnum = ""
        if(temp != -1):
            nextnum = int(index)
            print(nextnum)
    