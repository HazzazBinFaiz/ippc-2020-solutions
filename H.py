for t in range(int(input())):
    path = input()
    left = (0, 1)
    right = (1, 0)
    up = 1
    down = 1
    for p in path:
        if p == 'R':
            left = (up, down)
        else:
            right = (up, down)
        up = right[0] + left[0]
        down = right[1] + left[1]
    print("{}/{}".format(up, down))
