nota = int(input("Digite sua nota: "))

if nota >= 9 and nota < 10:
    print("A")

elif nota >= 7 and nota < 9:
    print("B")

elif nota >= 5 and nota < 7:
    print("C")

elif nota >= 3 and nota < 5:
    print("D")

elif nota >= 0 and nota < 3:
    print("E")

else:
    print("Nota fora do intervalo")
