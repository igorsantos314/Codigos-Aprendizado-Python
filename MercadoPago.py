

class mercado:

    def __init__(self, valor, parcelas, pagamento):

        self.jurosParcelas          = [0, 0, 0.0409, 0.0541, 0.0670, 0.0796, 0.0920, 0.1041, 0.1161, 0.1278, 13.92, 0.1505, 0.1615]
        self.jurosLiberacaoDinheiro = [5.31, 0.0436, 0.0360]

        self.valor = valor
        self.parcelas = parcelas
        self.pagamento = pagamento

    def getValor(self):
        return self.valor

    def getParcelas(self):
        return self.parcelas
    
    def getPagamento(self):
        return self.pagamento

    def getJurosParcelas(self):
        return self.jurosParcelas

    def getJurosLiberacaoDinheiro(self):
        return self.jurosLiberacaoDinheiro

    def calcValorTotal(self):
        
        #juros das parcelas em R$
        jp = self.getValor() * self.jurosParcelas[self.getPagamento()]

        #juros da forma de recebimento em R$
        formaRecebimento = self.getValor() * self.jurosLiberacaoDinheiro[self.getPagamento()]

        #valor total
        total = self.getValor() - jp - formaRecebimento

        #diferenca
        dif = jp + formaRecebimento

        return (total, dif)

a = mercado(100, 10, 0)
print(a.calcValorTotal())
