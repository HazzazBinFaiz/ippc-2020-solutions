num = int(input())
abs_num = abs(num)
summed = int((abs_num * (abs_num + 1)) / 2)
if num < 0:
    print(-summed+1)
else:
    print(summed)
