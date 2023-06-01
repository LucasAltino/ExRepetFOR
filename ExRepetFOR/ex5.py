velho = []
nomevelho = []
nova = []

for n in range(0,9):
    sexo = str(input("Digite seu sexo: (M ou F)"))
    if sexo == "M":
        nome = str("Digite seu nome: ")

        idade = int("Digite sua idade: ")

    elif sexo == "F":
        nome = str("Digite seu nome: ")
        idade = int("Digite sua idade: ")
        if idade < 20:
            nova.append(idade)

print("Quantidade de mulheres que tem menos de 20 anos: ", len(nova))