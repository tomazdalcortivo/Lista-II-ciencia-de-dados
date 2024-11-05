numeros = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
somador = 0 
for num in numeros: somador += num

print("A soma dos elementos da lista é:", somador)