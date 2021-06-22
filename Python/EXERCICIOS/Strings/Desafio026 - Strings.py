# ESCREVA UMA FRASE E VALIDE QTD DE LETRAS "A", A PRIMEIRA e ULTIMA POSIÇÃO EM QUE ELA APARECE:

frase = str(input('Digite uma frase... ')).upper().strip()

print(f'A letra "A" aparece {frase.count("A")}X na frase "{frase}"')
print(f'A letra "A" aparece pela 1° vez na posição {frase.find("A")+1} na frase "{frase}"')
print(f'A letra "A" aparece pela ultima vez na posição {frase.rfind("A")+1} na frase "{frase}"')