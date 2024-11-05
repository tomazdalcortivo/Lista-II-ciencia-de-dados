numeros = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

nao_duplicatas = []

for num in numeros:
    if num not in nao_duplicatas:
        nao_duplicatas.append(num)


print("A lista sem duplicatas é:", nao_duplicatas)