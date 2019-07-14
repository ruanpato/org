import Bloco
import MemoriaCache

class Linha:
    def __init__(self, bloco):
#        self.rotulo = # calculoRotuloBaseadoNoMapeamento
        self.endereco = bloco.endereco
        self.valor = bloco.valor

