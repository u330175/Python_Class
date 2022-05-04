a=[330, 360, 320, 410, 350, 490, 810, 220, 230, 180, 240]
sum=0
for index in a:
    if(sum < 3000):
       sum=sum+index
       print("今年被動收入%d，目前累積退休金%d" % (index, sum))
       #break
    else:
        print("退休金%d已達3000萬退休了" % (sum))
        #break
        