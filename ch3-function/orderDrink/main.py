import bar

drinkList = ['啤酒', '葡萄酒 ', '香檳 ', '清酒 ', '白蘭地 ', '威士忌', '高粱酒', '伏特加', '萊姆酒', '琴酒']

# 1. 亂數產生99筆酒類點單儲存串列回傳

orderList = bar.randomDrink(drinkList)

# 2. 統計每種酒有多少單
staticList = bar.staticDrink(orderList)
print(staticList)