# Entrada do salário bruto
salario_bruto = float(input('Digite seu salário bruto: '))

# Entrada das horas extras
hora_extra = float(input('Digite quantas horas extras você fez: '))

# LOOP para garantir que dependentes seja número inteiro
while True:
    try:
        dependentes = int(input('Digite o número de dependentes (somente inteiros): '))
        break
    except ValueError:
        print('Erro! Digite um número inteiro.')

# Plano de saúde como booleano
plano_de_saude = input('Possui plano de saúde? (True/False): ').strip().lower()

if plano_de_saude == 'true':
    plano_saude = 150
    plano_de_saude = True
else:
    plano_de_saude = False

# Exibe situação dos dependentes
if dependentes > 0:
    print('Tem dependentes.')
else:
    print('Não tem dependentes.')

# Exibe situação do plano de saúde
if plano_de_saude:
    print('Tem plano de saúde.')
else:
    print('Não tem plano de saúde.')


# Descontos simples (como seu código original)

inss = 8/100
fgts = 7.5/100

# Cálculo do salário líquido
valor_liquido = salario_bruto - plano_saude - (salario_bruto * inss) - (salario_bruto * fgts)

# --- CÁLCULO DA HORA EXTRA ---
# Considerando salário-hora baseado em 220h mensais
salario_hora = salario_bruto / 220

# Hora extra com adicional de 50%
valor_hora_extra = hora_extra * (salario_hora * 1.5)

# Soma no salário líquido
valor_liquido += valor_hora_extra

print('\n--- RESULTADO FINAL ---')
print(f'Salário líquido sem horas extras: {salario_bruto - plano_saude - (salario_bruto * inss) - (salario_bruto * fgts):.2f}')
print(f'Valor das horas extras: {valor_hora_extra:.2f}')
print(f'Salário líquido final + horas extras: {valor_liquido:.2f}')
