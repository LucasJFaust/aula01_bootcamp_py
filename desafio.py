# Constante do Bonus de 2024

CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus_usuario = float(input("Difite o valor do seu Bonus: "))

# 4) Calcule o valor do bônus final

valor_final = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuário {nome_usuario}, tem o valor do seu salário de:{salario_usuario}, o seu bonus foi de:{bonus_usuario}, logo, o valor final foi de:{valor_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?