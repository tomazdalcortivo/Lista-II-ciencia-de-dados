num1 = int(input("Digite a numero um"))
num2 = int(input("Digite a numero dois"))

soma = 0 
while(num1 <= num2):
    if num1 % 3 == 0: 
        soma += num1
    num1 += 1 

print("A soma dos múltiplos de 3 entre os números fornecidos é:", soma)
