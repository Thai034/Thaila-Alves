#Thaila da Silva Alves

valor = float(input("Insira o valor do produto: "))

res = valor - (valor * 0.30)
print(f"O produto com 30% de desconto, custará R${res:.2f}")

#Gabarito da questão
'''
valor = float(input("Insira o valor do produto: "))
valor_com_desconto = valor - (valor * 30 / 100)

print(f"O produto com 30% de desconto, custará R$ {valor_com_desconto:.2f}")
'''