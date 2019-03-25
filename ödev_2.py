import random

#Hassasiyetimiz on üzeri dokuz

def f(x):
    return x**2-6*x+8

def df(x):
    return 2*x-6

x1 = int(input("başlangıç tahmini: "))
x2 = int(input("bitiş tahmini: "))

def Yarıya_bölme_yöntemi(x1, x2):
    if(f(x1)*f(x2) == 0):
        print("bildiniz")
    elif(f(x1)*f(x2) > 0):
        print("tek sayıda kök yok")
    else:
        for i in range(1000):
            xr = (x1+x2)/2
            if(int(f(xr)*pow(10, 9)) == 0):
                print("Yarıya bölme yöntemi - ""kok: ", xr, i, "adımda")
                break
            elif(f(x1)*f(xr)<0):
                x2 = xr
            else:
                x1 = xr


def Dogruya_yaklaştırma_yöntemi(x1, x2):
    if (f(x1) * f(x2) == 0):
        print("bildiniz")
    elif (f(x1) * f(x2) > 0):
        print("bu değer aralığında tek bir kök yok.")
    else:
        for i in range(1000):
            xr = (f(x2)*x1-f(x1)*x2)/(f(x2)-f(x1))
            if (int(f(xr)*pow(10, 9)) == 0 ):
                print("Doğruya yaklaştırma yöntemi - ", "kok: ", xr, i, "adımda")
                break
            elif (f(x1) * f(xr) < 0):
                x2 = xr
            else:
                x1 = xr


def Newton_yöntemi(x1, x2):
    if (f(x1) * f(x2) == 0):
        print("bildiniz")
    elif (f(x1) * f(x2) > 0):
        print("bu değer aralığında tek bir kök yok.")
    else:
        x0 = random.randint(x1, x2)                  #rastgele başlangıç değeri atıyoruz
        xn = x0 - f(x0)/df(x0)
        for i in range(1000):
            if (int(f(xn)*pow(10, 9)) == 0):
                print("Newton yöntemi - ""kok: ", xn, i, "adımda")
                break
            elif (f(x1) * f(xn) < 0):
                x2 = xn
            else:
                x1 = xn
            xn = xn - f(xn)/df(xn)


Yarıya_bölme_yöntemi(x1, x2)
Dogruya_yaklaştırma_yöntemi(x1, x2)
Newton_yöntemi(x1, x2)
