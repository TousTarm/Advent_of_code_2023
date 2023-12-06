with open("2/input.txt",newline="\n") as file:
    line = file.readlines()

total = 0

for index,aaa in enumerate(line):
    aaa = aaa.replace("\n","")
    newline = aaa.replace("Game " + str(index + 1) + ":","")
    newline = newline.split(";")
    out = True
    blue = 0
    red = 0
    green = 0
    hblue = 0
    hred = 0
    hgreen = 0
    for word in newline:
        blue = 0
        red = 0
        green = 0
        newword = word.split(",")
        for i in newword:
            value = i.find("blue")
            if(value != -1):
                temp = [int(x) for x in i.split() if x.isdigit()]
                blue += int(temp[0])
                if (blue>hblue):
                    hblue = blue
            value = i.find("red")
            if(value != -1):
                temp = [int(x) for x in i.split() if x.isdigit()]
                red += int(temp[0])
                if (red>hred):
                    hred = red
            value = i.find("green")
            if(value != -1):
                temp = [int(x) for x in i.split() if x.isdigit()]
                green += int(temp[0])
                if (green>hgreen):
                    hgreen = green
    print(index+1,hblue,hgreen,hred)

    if(out == True):
        total += hblue * hgreen * hred
print(total)