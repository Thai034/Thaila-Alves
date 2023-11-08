#Thaila da Silva Alves

print("Digite suas médias abaixo para tirarmos a média e ver se vocÊ passou!")

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))
nota3 = float(input("Informe sua terceira nota: "))
nota4 = float(input("Informe sua quarta nota: "))
nota5 = float(input("Informe sua quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (media >= 70):
    print(f"Sua média é {media}, Você está Aprovada!")

else:
    print(f"Sua média é {media}, Sinto muito, Você está reprovado!")



#gabarito da questão
'''
print("Digite suas médias abaixo para tirarmos a média e ver se vocÊ passou!")

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))
nota3 = float(input("Informe sua terceira nota: "))
nota4 = float(input("Informe sua quarta nota: "))
nota5 = float(input("Informe sua quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (media >= 70):
    situação = "Aprovado"

else:
    situação = "Reprovado"
    
print(f"Sua média é {media:.1f} - Sinto muito, Você está {situação}!")
'''