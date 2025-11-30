class Funcionario:
    def __init__(self, salario_bruto, horas_extras, dependentes, plano_saude):
        self.salario_bruto = salario_bruto
        self.horas_extras = horas_extras
        self.dependentes = dependentes
        self.plano_saude = plano_saude

        self.valor_plano = 150 if plano_saude else 0  # ✅ DESCONTO DO PLANO
        self.inss = 0.08
        self.fgts = 0.075

    def calcular_salario_liquido(self):
        desconto_inss = self.salario_bruto * self.inss
        desconto_fgts = self.salario_bruto * self.fgts
        bonus_dependentes = self.dependentes * 100

        salario_liquido = (
            self.salario_bruto
            - self.valor_plano          # ✅ DESCONTO DO PLANO APLICADO
            - desconto_inss
            - desconto_fgts
            + bonus_dependentes
        )

        return salario_liquido

    def calcular_horas_extras(self):
        salario_hora = self.salario_bruto / 220
        return self.horas_extras * (salario_hora * 1.5)

    def salario_final(self):
        return self.calcular_salario_liquido() + self.calcular_horas_extras()


# ---------------- ENTRADAS ----------------

salario_bruto = float(input('Digite seu salário bruto: '))
hora_extra = float(input('Digite quantas horas extras você fez: '))

while True:
    try:
        dependentes = int(input('Digite o número de dependentes: '))
        break
    except ValueError:
        print('Digite apenas números inteiros!')

plano = input('Possui plano de saúde? (True/False): ').strip().lower()
plano_saude = True if plano == 'true' else False


if plano in ['sim', 's', 'true', 't']:
    plano_saude = True
elif plano in ['nao', 'não', 'n', 'false', 'f']:
    plano_saude = False
else:
    print('Resposta inválida! Considerado como NÃO.')
    plano_saude = False

# ---------------- USO DA CLASSE ----------------

funcionario = Funcionario(
    salario_bruto,
    hora_extra,
    dependentes,
    plano_saude
)

salario_liquido = funcionario.calcular_salario_liquido()
valor_hora_extra = funcionario.calcular_horas_extras()
salario_final = funcionario.salario_final()

print('\n--- RESULTADO FINAL ---')
print(f'Dependentes: {dependentes} (+ R$ {dependentes * 100:.2f})')
print(f'Tem plano de saúde? {plano_saude}')
print(f'Desconto do plano: R$ {funcionario.valor_plano:.2f}')
print(f'Salário líquido sem horas extras: R$ {salario_liquido:.2f}')
print(f'Valor das horas extras: R$ {valor_hora_extra:.2f}')
print(f'Salário líquido final: R$ {salario_final:.2f}')
