def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro! Digite um número válido.")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro! Digite apenas números inteiros.")


def ler_booleano(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["true", "sim"]:
            return True
        elif resposta in ["false", "nao", "não"]:
            return False
        else:
            print("Digite apenas True/False ou Sim/Não.")


def calcular_salario_liquido(salario_bruto, horas_extras, plano_saude):
    inss = 0.08
    fgts = 0.075
    desconto_plano = 150 if plano_saude else 0

    salario_hora = salario_bruto / 220
    valor_hora_extra = horas_extras * (salario_hora * 1.5)

    salario_liquido = (
        salario_bruto
        - desconto_plano
        - (salario_bruto * inss)
        - (salario_bruto * fgts)
        + valor_hora_extra
    )

    return salario_liquido, valor_hora_extra


# ------------------ PROGRAMA PRINCIPAL ------------------

salario_bruto = ler_float("Digite seu salário bruto: ")
hora_extra = ler_float("Digite quantas horas extras você fez: ")
dependentes = ler_inteiro("Digite o número de dependentes: ")
plano_de_saude = ler_booleano("Possui plano de saúde? (True/False): ")

# Exibição das condições
print("\n--- SITUAÇÃO ---")
print("Tem dependentes." if dependentes > 0 else "Não tem dependentes.")
print("Tem plano de saúde." if plano_de_saude else "Não tem plano de saúde.")

salario_liquido, valor_hora_extra = calcular_salario_liquido(
    salario_bruto, hora_extra, plano_de_saude
)

print("\n--- RESULTADO FINAL ---")
print(f"Valor das horas extras: {valor_hora_extra:.2f}")
print(f"Salário líquido final: {salario_liquido:.2f}")
