""" 2 x 2 'lik matrisler için """

def determinand_two_by_two(liste):
    yeni = [[], []]
    for j in range(1, -1, -1):
        for i in range(len(liste[0])):
            if j == 1:
                yeni[j].append(liste[j][i] - liste[1][0]/liste[0][0] * liste[0][i])
            else:
                yeni[j].append(liste[j][i] - liste[0][1]/yeni[1][1] * yeni[1][i])

    print("2x2'lik matris\n", "Y değişkeninin değeri : ", yeni[1][2]/yeni[1][1], "  X değikeninin değeri : ", yeni[0][2]/yeni[0][0])


""" N x N matrisler için """

def determinand_N_by_N(liste):
    list = liste.copy()
    satir = len(liste)
    sütun = len(liste[0])

    for k in range(satir-1):                            # Satirları dolaşan döngü.
        for i in range(satir-1-k):                      # Sütunları sıfır yapılacak en son değişkene kadar dolaşan döngü.
            carpan = list[i][k]/list[i+1][k]
            for j in range(sütun):                      # Sütunları çarpan ile çarpmak için dolaşan döngü.
                list[i][j] += -carpan * list[i+1][j]

    
    print("\nsol üçgen matris", list)

                                            
    for p in range(satir-1, 0, -1):
        for t in range(satir-1, satir-1-p, -1):
            carpan = list[t][p]/list[t-1][p]
            for h in range(sütun):
                list[t][h] += -carpan * list[t-1][h]

      

    print("köşegen matris", list, "\n")

    for o in range(satir-1, -1, -1):
            print(satir-o, ". değişken değeri =", liste[o][satir] / liste[o][satir-o-1])


liste_2 = [[2, 3, 5], [4, 8, 20]]
determinand_N_by_N(liste_2)
