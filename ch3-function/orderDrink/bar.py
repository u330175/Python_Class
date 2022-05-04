import random
# 亂數產生酒的訂單
def randomDrink(drinkList):
    orderList=[]
    for index in range(99):
        t = random.randint(0, 9)
        orderList.append(drinkList[t])
    return orderList

# 統計酒的訂單數量
def staticDrink(orderList):
    staticList={}
    for index in orderList:
        if(index in staticList):
            staticList[index]+=1
        else:
            staticList[index]=1
    return  staticList