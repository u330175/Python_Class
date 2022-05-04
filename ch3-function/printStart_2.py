def printStar(i, character):
    for x in range(1, i+1):
        for y in range(x):
            print("%s" % (character) , end='')
        print("")    


x = input("請輸入列印行數")
c= input("請輸入字元")
printStar(int(x), c)       