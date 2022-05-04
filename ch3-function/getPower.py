def getPower(base, times):
    temp=1
    for i in range(times):
        temp = temp * base
    return temp


value = getPower(2, 3)
print(value)