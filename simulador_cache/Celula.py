class Celula:
    def __init__(self, endereco, valor):
        self.endereco = endereco
        self.valor = Dado(valor) # Ex: 00000000 || 0xf || 19
