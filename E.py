def summer(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0]+summer(array[1:])


for t in range(int(input())):
    lst = list(map(int, input().split()))
    print("Case {}: {}".format(t+1, summer(lst[1:])))
