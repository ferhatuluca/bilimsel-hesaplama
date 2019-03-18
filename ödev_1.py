""" 2 x 2 'lik matrisler için """
def denklem(liste):
    yeni = [[], []]
    for j in range(1, -1, -1):
        for i in range(len(liste[0])):
            if j == 1:
                yeni[j].append(liste[j][i] - liste[1][0]/liste[0][0] * liste[0][i])
            else:
                yeni[j].append(liste[j][i] - liste[0][1]/yeni[1][1] * yeni[1][i])

    print("Y değişkeninin değeri : ", yeni[1][2]/yeni[1][1], "  X değikeninin değeri : ", yeni[0][2]/yeni[0][0])


liste = [[2, 3, 7], [4, 2, 8]]
denklem(liste)

""" N x N matrisler için """

def denklem(liste):
    list = liste.copy()
    satir = len(liste)
    sütun = len(liste[0])
    
    for k in range(satir-1):
        for i in range(satir-1-k):
            carpan = list[i][k]/list[i+1][k]
            for j in range(sütun):
                list[i][j] += -carpan * list[i+1][j]


    print("sol üçgen matris", list, "\n")
    
    count = 0                                   # Matriste en alt satırdan üst satırlara gidilmesi için gereken değişken.
    for p in range(satir-1, 0, -1):
        for t in range(satir-1, count, -1):
            carpan = list[t][p]/list[t-1][p]
            for h in range(sütun):
                list[t][h] += -carpan * list[t-1][h]

        count += 1
        
    print("köşegen matris", list, "\n")

    for o in range(satir-1, -1, -1):
            print(satir-o, ". değişken değeri =", liste[o][satir]/liste[o][satir-o-1])


liste = [[1, 2, 7, 4, 2, 4], [2, 5, 6, 7, 1, 3], [7, 8, 9, 10, 2, 12], [8, 1, 4, 3, 2, 21], [3, 5, 7, 2, 3, 2]]
denklem(liste)

