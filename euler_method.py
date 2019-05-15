def f(x, y):
    return -y/x

h = float(input("h gir"))
yson = int(input("yson"))
y4 = 3/4
def euler(h, yson, y4):
    for i in range(4, yson):
        y4 = y4 + f(i, y4)*h
        print(y4)
    print(y4)

#iyileştirilmiş
def improved_euler(h, yson, y4):
    i = 4
    for i in range(4, yson):
        ybucuk = y4 + f(i, y4) * h/2
        y4 = y4 + f(i+1/2, ybucuk) * h
    print(y4)
    
euler(h, yson, y4)
