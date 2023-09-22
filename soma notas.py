def Media(notas):
    s = 0
    for i in notas:
        s = s + i
    print(s/3)
notas = []
for x in range(0,3):
    nota = float(input('Digite três notas:'))
    notas.append(nota)
Media(notas)

