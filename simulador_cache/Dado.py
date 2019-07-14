class Dado:
    def __init__(self, bits, valor, base):
        self.bits = bits                # Quantidade em decimal de quantos bits que o o valor pode ter.
        self.base = base                # Base a qual o dado foi passado e a qual vai ser exibido por padrão, base 0 é Caractere.
        self.decimal = int(valor)       # Valor na base decimal.
        self.hexadecimal = hex(valor)   # Valor na base hexadecimal.
        self.binario = bin(int(valor))  # Valor na base binária.
        self.normalizaBinario()         # Normaliza o binário.
        #self.verificaCapacidade()       # Verifica a capacidade.
    
    def verificaCapacidade(self):           # Função que verifica se o dado não tem os bits necessários para representar este valor.
        if(len(self.binario) > self.bits):  # Verifica se o dado não tem os bits necessários para representar este valor.
            return False                    # Não é possível representar.
        return True                         # É possível representar.

    def normalizaBinario(self):         # Função que normaliza a quantidade de bits na representação binária.
        self.binario = self.binario[2:] # Tira o 0b
        zerosExtras = '0'               # Inicia a variável.
        if(len(self.binario) < self.bits):                      # Verifica se necessita 'normalizar.
            for i in range(self.bits-1-len(self.binario)):
                zerosExtras = zerosExtras + '0'                 # Incrementa a quantidade necessária de zeros.
            self.binario = zerosExtras + self.binario           # Coloca o valor normalizado.
    
    def exibeDados(self):               # Exibe os dados
        print("Base:", self.base, "\nQuantidade de bits para representação:", self.bits, "\nValor Decimal:", self.decimal, "\nValor Hexadecimal:", self.hexadecimal, "\nValor Binário:", self.binario)
