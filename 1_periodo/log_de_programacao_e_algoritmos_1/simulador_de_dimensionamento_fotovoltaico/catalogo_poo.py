# catalogo_poo.py by Antônio (AntonioOliveira-Web)

# #CLASSES PARA CADA TIPO DE PRODUTO PARA CRIAR O CATALAGO

class PainelSolar:
    def __init__(self, modelo, potencia_kw, preco):
        self.modelo = modelo
        self.potencia_kw = potencia_kw
        self.preco = preco
        
class Inversor:
    def __init__(self, modelo, potencia_kw, preco):
        self.modelo = modelo
        self.potencia_kw = potencia_kw
        self.preco = preco
        
class Bateria:
    def __init__(self, modelo, capacidade_ah, tensao_v, preco):
        self.modelo = modelo
        self.capacidade_ah = capacidade_ah
        self.tensao_v = tensao_v
        self.preco = preco
        
#OBJETOS DO CATALOGO

paineis = [
    PainelSolar("Painel 450w", 0.45, 900),
    PainelSolar("Painel 550w", 0.55, 1200),
]

inversores = [
    Inversor("Inversor 3kw", 3, 4000),
    Inversor("Inversor 5kw", 3, 6000),
]

baterias = [
    Bateria("Bateria 150Ah 24V", 150, 24, 3500),
    Bateria("Bateria 200Ah 48V", 200, 48, 6000),
]