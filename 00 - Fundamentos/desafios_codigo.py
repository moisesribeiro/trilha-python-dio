def calcular_imposto(salario):
    aliquota = 0.00
    if salario >= 0 and salario <= 1100:
        aliquota = 0.05
        
    elif salario > 1100 and salario <= 2500:
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

# Obtendo os valores do usuário
salario = float(input("Digite seu salário: "))
beneficios = float(input("Digite o valor dos benefícios: "))

# Calculando o imposto
imposto = calcular_imposto(salario)

# Exibindo o resultado
print("O valor do salário bruto é:", salario - imposto + beneficios)