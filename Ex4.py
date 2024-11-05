frase = input("Digite uma frase: ")

contador_vogais = 0


vogais = "aeiouAEIOU"

for caractere in frase:
    if caractere in vogais:
        contador_vogais += 1

print("O número de vogais na frase é:", contador_vogais)