def printStar(i):
    for x in range(1, i+1):
        for y in range(x):
            print("*", end='')
        print("")    


x = input("請輸入列印行數")
printStar(int(x))