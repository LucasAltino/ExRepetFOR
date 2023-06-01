somam = 0
somaf = 0
qm = 0
qf = 0
listaf = []
listam = []
for n in range(1,11):
    z = str(input("Digite seu sexo: (M ou F) "))
    if z == "M":
        y = int(input("Digite sua idade: "))
        somam += y
        listam.append(somam)
    if z == "F":
        y = int(input("Digite sua idade: "))
        somaf += y
        listaf.append(somaf)

print("Média idade feminina: ", somaf/len(listaf))
print("Média idade masculina: ", somam/len(listam))
print("Média de todas as idade: ", (somaf + somam)/10)