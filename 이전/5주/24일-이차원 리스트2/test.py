d_y = [0, 0, 1 ,-1]
d_x = [1, -1, 0, 0]
y,x = 1, 1
for d in range(4):
    find_y = y +d_y[d]
    find_x = x + d_x[d]
    print(find_y, find_x)