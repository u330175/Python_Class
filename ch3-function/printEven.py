def printEven(x):
    if(x%2==0):
        return "偶數"
    else:
        return "奇數"


x=input("輸入一個整數")
s = printEven(int(x))
print(s)