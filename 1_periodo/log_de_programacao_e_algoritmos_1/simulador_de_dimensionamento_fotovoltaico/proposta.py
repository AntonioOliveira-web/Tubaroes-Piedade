# proposta.py
from crm import coletar_dados
from motor_solar import *

# Coleta os dados do cliente
(
    nome,
    media_consumo,
    hsp,
    preco_painel,
    potencia_painel,
    tarifa,
    inversor,
    mao_obra,
) = coletar_dados()

# Calcula consumo diário
consumo_diario = calc_consumo_diario(media_consumo)

# Calcula potência do sistema (kWp)
kwp_total = pot_pico_kwp(consumo_diario, hsp)

# Calcula quantidade de painéis
qtd_paineis = calc_paineis(kwp_total, potencia_painel)

# Calcula custo total
custo_total = calc_custo_total(
    qtd_paineis,
    preco_painel,
    inversor,
    mao_obra
)

# Calcula economia mensal
economia = calc_economia(media_consumo, tarifa)

# Calcula payback
payback = calc_payback(custo_total, economia)

# Tipo do sistema
tipo_sistema = "On-Grid"

# Imprime relatório
# relatorio.py

def imprimir_relatorio(
    nome_cliente,
    tipo_sistema,
    kwp_total,
    qtd_paineis,
    preco_painel,
    inversor,
    mao_obra,
    economia_mensal,
    payback,
):

    custo_paineis = qtd_paineis * preco_painel
    custo_total = custo_paineis + inversor + mao_obra

    print("\n" + "=" * 45)
    print(f"{'RELATÓRIO DO SISTEMA SOLAR':^45}")
    print("=" * 45)

    print(f"{'Cliente:':<20} {nome_cliente}")
    print(f"{'Sistema:':<20} {tipo_sistema}")

    print("-" * 45)

    print(f"{'Potência (kWp):':<20} {kwp_total:.2f} kWp")
    print(f"{'Qtd. Painéis:':<20} {qtd_paineis}")

    print("-" * 45)

    print(f"{'Painéis:':<20} R$ {custo_paineis:.2f}")
    print(f"{'Inversor:':<20} R$ {inversor:.2f}")
    print(f"{'Mão de Obra:':<20} R$ {mao_obra:.2f}")

    print("-" * 45)

    print(f"{'Custo Total:':<20} R$ {custo_total:.2f}")
    print(f"{'Economia Mensal:':<20} R$ {economia_mensal:.2f}")
    print(f"{'Payback:':<20} {payback:.1f} meses")

    print("=" * 45)