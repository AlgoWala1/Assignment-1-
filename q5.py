import math
for angle in range(0,360,15):
    print(angle," ...... ",round(math.sin((angle*3.14)/180),4),"   ",round(math.cos((angle*3.14)/180),4))
