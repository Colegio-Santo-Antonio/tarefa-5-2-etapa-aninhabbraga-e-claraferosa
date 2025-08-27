números = input()
impares = []
for i in numeros [-1::-2]:
    impares.append(int(i))
pares = []
for i in numeros [-2::-2]:
    if 2*int (i)>10:
        pares.append((2*int(i)-10+1))
    else:
        pares.append(2*int(i))
soma = sum(impares)+sum(pares)
if int(soma/10) == soma/10:
  print("Cartão Válido")
else:
  print("Cartão Inválido")
  
# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
