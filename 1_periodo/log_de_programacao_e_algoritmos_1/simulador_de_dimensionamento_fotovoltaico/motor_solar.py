# motor_solar.py by Vitor (Vit0ncio)

# Função que calcula o consumo diário
def calc_consumo_diario(consumo_mensal):
    return consumo_mensal / 30


# Função que calcula o kWp
def pot_pico_kwp(consumo_diario, hsp):
    if hsp == 0:
        return None

    return consumo_diario / (hsp * 0.8)


# Função que calcula os painéis
def calc_paineis(kwp_total, potencia_painel_w):
    if potencia_painel_w == 0:
        return None

    potencia_painel_w = potencia_painel_w / 1000
    resultado = kwp_total / potencia_painel_w

    # Aqui ele pega o resultado que mostrará a quantidade de painéis
    # Para não permitir números quebrados e se tiver, arredondar pra mais
    # O código converte o resultado para int (ex 4.3 vira 4) e compara os valores
    # Caso o resultado seja um número quebrado e seja maior que o número convertido para inteiro
    # Ele transforma o número e inteiro e acrescenta em 1
    if resultado > int(resultado):
        qtd_paineis = int(resultado) + 1
    else:
        qtd_paineis = int(resultado)

    return qtd_paineis


# Função que calcula o custo total
def calc_custo_total(qtd_paineis, preco_painel, inversor, mao_obra):
    return (qtd_paineis * preco_painel) + inversor + mao_obra


# Função que calcula a economia
def calc_economia(consumo_mensal, tarifa):
    return consumo_mensal * tarifa


# Função que calcula o payback
def calc_payback(custo_total, economia_mensal):
    return custo_total / economia_mensal


# Função que calcula o banco de baterias
def calc_banco_bat(consumo_diario, autonomia, tensao):
    return (consumo_diario * 1000 * autonomia) / (tensao * 0.80)
