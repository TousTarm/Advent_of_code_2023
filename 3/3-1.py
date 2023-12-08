with open("3/input.txt",newline="\n") as file:
    file = file.readlines()

total = 0
for index,line in enumerate(file):
    charnum=0
    while(charnum<len(line)):
        ftop = False 
        fbottom = False
        fright = False
        fleft = False
        number = ""
        print(index,line[charnum])
        while(line[charnum].isdigit()):
            number += str(line[charnum])
            charnum+=1
        if(not line[charnum].isdigit() and line[charnum-1].isdigit()):
            for offest in range(len(number) + 2):
                if(charnum-len(number)-1 + offest >= 0) and index-1>=0 and (charnum + offest < len(line)):
                    xxx = file[index-1][charnum-len(number)-1 + offest]
                    if(xxx != "." and not xxx.isdigit()):
                        ftop = True

                        print("nad",index + 1,number,xxx)

                if(charnum-len(number)-1 + offest >= 0) and index+1<len(file) and (charnum + offest < len(line)):
                    xxx = file[index+1][charnum-len(number)-1 + offest]
                    if(xxx != "." and not xxx.isdigit()):
                        fbottom = True
                        print("pod",index + 1,number,xxx)

            if(charnum-len(number)-1 >= 0):
                xxx = file[index][charnum-len(number)-1]
                if(xxx != "." and not xxx.isdigit()):
                    fleft = True
                    print("left",index + 1,number,xxx,charnum-len(number)-1)

            if(charnum + 1< len(line)):
                xxx = file[index][charnum]
                if(xxx != "." and not xxx.isdigit()):
                    fright = True
                    print("right",index + 1,number,xxx)
        charnum+=1

        if ftop == True or fbottom == True or fright == True or fleft == True:
           total += int(number)
        
print("total is",total)