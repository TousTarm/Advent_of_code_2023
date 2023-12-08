with open("3/input-test.txt",newline="\n") as file:
    file = file.readlines()

def check(x):
    #topcheck
    if(index-1>=0):
        for i in range(3):
            print(x-i)
            if(file[index-1][x-i]).isdigit():
                numindex = file[index-1][x-i]
                

    #botcheck
    """
    if(index+1<=len(file)):
        for i in range(3):
            if(file[index+1][x-1+i]).isdigit():
                print("bottom charnum",x-1+i)
    """

total = 0
for index,line in enumerate(file):
    charnum=0
    while(charnum<len(line)):
        number = ""
        if(line[charnum]) == "*":
            location = line[charnum]
            check(charnum)
        charnum+=1
        
print("total is",total)