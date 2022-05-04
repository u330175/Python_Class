import time

localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
print(result)