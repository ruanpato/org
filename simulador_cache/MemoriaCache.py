import Linha

class MemoriaCache:
    def __init__(self, mapeamento, linhasConjuntos):
        self.mapeamento = mapeamento # 0 Para direto, 1 para associativo por conjuntos
        self.linhas = linhas         # Linhas
        self.conjuntos = conjuntos   # Conjuntos
        pass


def politicaSubstituicao(self, politica):
    if politica == 0: # LRU (Least Recently Used)
        self.LRU()
    elif politica == 1: # RR (Random Replacement)
        self.RR()
    elif politica == 2: # LFU (Least Frequently Used)
        self.LFU()
        elif politica == 3: # Belady
