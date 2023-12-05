with open('input1.txt',newline="\n") as file:
    line = file.readlines()

result = []
number = []
words = ["one","two","three","four","five","six","seven","eight","nine"]

for i in range(len(line)):
    word = line[i]
    number.append("")
    arr1 = []
    tempindex = []
    for index, strword in enumerate(words):
        for a in range(len(word)):
            temp = word.find(strword,a,len(word))
            if(temp != -1) and (temp not in tempindex):
                tempindex.append(temp)
                x = [temp,index+1,len(strword)]
                arr1.append(x)
                print(temp)
    arr1.sort()
    print(arr1)
    newword = ""
    dd = 0
    for x in range(len(word)):
        if(word[x].isdigit()):
            newword += word[x]
        elif(len(arr1)>0) and (x == arr1[dd][0]):
            print(len(arr1),dd)
            for y in range(arr1[dd][2]):
                newword += str(arr1[dd][1])
            x+=arr1[dd][2]
            if(dd+1<len(arr1)):
                dd+=1
        if(x >= len(word)):
            break
    number[i] = newword

for i in range(len(number)):
    result.append(int(number[i][0]) * 10 + int(number[i][-1]))
print(result)

total = 0
for i in range(len(result)):
    total += int(result[i])
print(total)