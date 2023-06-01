fim = int(input("Digite a quantidade de pacientes para serem analisados: "))
soma = 0
for n in range(1,fim+1):
    z = float(input("Digite sua temperatura corporal: "))
    soma += z

    if z < 37.2:
        print("Normal")
    elif z > 37.3 and z < 38:
        print("Estado febril")
    elif z > 38 and z < 39:
        print("Febre")
    else:
        print("Febre Alta")

print("Quantidade de pacientes analisados:",fim)
print("Média", soma/fim)