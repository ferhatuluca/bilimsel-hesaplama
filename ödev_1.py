def denklem(liste):
    yeni = [[], []]
    for j in range(1, -1, -1):
        for i in range(len(liste[0])):
            if j == 1:
                yeni[j].append(liste[j][i] - liste[1][0]/liste[0][0] * liste[0][i])
            else:
                yeni[j].append(liste[j][i] - liste[0][1]/yeni[1][1] * yeni[1][i])

    print("Y değişkeninin değeri : ", yeni[1][2]/yeni[1][1], "  X değikeninin değeri : ", yeni[0][2]/yeni[0][0])


liste = []
print("1. denklemin katsayılarını ve sabit sayısını giriniz")
liste.append([int(input()), int(input()), int(input())])
print("2. denklemin katsayılarını ve sabit sayısını giriniz")
liste.append([int(input()), int(input()), int(input())])
print("\n")

denklem(liste)
