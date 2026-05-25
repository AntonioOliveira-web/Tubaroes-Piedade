# main.py by Arthur (arthurrqueiroz)

# Importa as funções do crm.py e do motor_solar.py
from crm import coletar_dados
from motor_solar import *  # O * serve pra importar todas as funções do arquivo
from proposta import imprimir_relatorio


# Função principal
def main():
    print("--- SIMULADOR FOTOVOLTAICO ---")

    # Chamada de algumas variáveis do crm.py
    (
        nome_cliente,
        media_consumo,
        hsp,
        preco_painel,
        potencia_painel,
        tarifa,
        inversor,
        mao_obra,
    ) = coletar_dados()

    # Chamada das funções para os cálculos
    consumo_diario = calc_consumo_diario(media_consumo)
    pot_pico = pot_pico_kwp(consumo_diario, hsp)
    qtd_paineis = calc_paineis(pot_pico, potencia_painel)
    custo_total = calc_custo_total(qtd_paineis, preco_painel, inversor, mao_obra)
    economia = calc_economia(media_consumo, tarifa)
    payback = calc_payback(custo_total, economia)

    # Se a quantidade de painéis der zero (ou null)
    # Ele mostra um erro
    if qtd_paineis is None:
        print("Erro no cálculo dos painéis.")
        return

    # Resultado
    print(f"Cliente: {nome_cliente}")
    print(f"Consumo diário: {consumo_diario} kWh")
    print(f"Potência pico: {pot_pico} kWp")
    print(f"Quantidade de painéis: {qtd_paineis}")
    print(f"Custo total: R$ {custo_total}")
    print(f"Economia mensal: R$ {economia}")
    print(f"Payback estimado: {payback} meses")
    
    print(imprimir_relatorio(
        nome_cliente,
        "On-Grid",
        pot_pico,
        qtd_paineis,
        preco_painel,
        inversor,
        mao_obra,
        economia,
        payback
    ))


# Inicia a função
main()
