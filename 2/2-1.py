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
            value = i.find("red")
            if(value != -1):
                temp = [int(x) for x in i.split() if x.isdigit()]
                red += int(temp[0])
            value = i.find("green")
            if(value != -1):
                temp = [int(x) for x in i.split() if x.isdigit()]
                green += int(temp[0])
        if(blue > 14) or (red > 12) or (green > 13):    
            out = False
            if(blue>14):
                print(index,"is not valid because blue =",blue)
            if(red>12):
                print(index,"is not valid because red =",red)
            if(green>14):
                print(index,"is not valid because green =",green)

    if(out == True):
        total += index + 1
print(total)