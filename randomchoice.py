from  random import  *

coin = ["人头","花"]
head_still_times=0
ten_head_times = 0
head_times=0

for i in range(1000000):
    if choice(coin)=="人头":
        head_times+=1
        head_still_times+=1
    else:
        head_still_times=0
    if head_still_times==10:
        ten_head_times+=1
        head_still_times=0


print("一共投了",head_times,"人头，连续10次为：",ten_head_times)
