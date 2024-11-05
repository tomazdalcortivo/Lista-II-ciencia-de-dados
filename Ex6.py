numeros = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

print("O maior número da lista é:", max(numeros))
print("O menor número da lista é:", min(numeros))