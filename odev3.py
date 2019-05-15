import math

def f(x, y):
    return 4-x**2-y**2
def g(x, y):
    return 1-math.exp(x)-y
def fx(x, y):
    return -2*x
def fy(x, y):
    return -2*y
def gx(x, y):
    return -math.exp(x)
def gy(x, y):
    return -1

def determinand_two_by_two(liste):
    carpan = liste[0][0] / liste[1][0]
    for i in range(3):
        liste[0][i] += -carpan*liste[1][i]
    carpan = liste[1][1] / liste[0][1]
    for i in range(3):
        liste[1][i] += -carpan*liste[0][i]
    return liste[1][2]/liste[1][0], liste[0][2]/liste[0][1]

def hesapla(numTrial):
    x0 = float(input("x in değeri"))
    y0 = float(input("y nin değeri"))
    matrix = [[fx(x0, y0), fy(x0, y0), -f(x0, y0)], [gx(x0, y0), gy(x0, y0), -g(x0, y0)]]
    degerler = determinand_two_by_two(matrix)
    print(degerler, x0, y0)
    for i in range(numTrial):
        x0 = x0 + degerler[0]
        y0 = y0 + degerler[1]
        matrix = [[fx(x0, y0), fy(x0, y0), -f(x0, y0)], [gx(x0, y0), gy(x0, y0), -g(x0, y0)]]
        degerler = determinand_two_by_two(matrix)
        print(degerler, x0, y0)
        
    print(x0**2 + y0**2)           # sağlama
    
liste_2 = [[3, 4, 5], [21, 12, 30]]
hesapla(10)
