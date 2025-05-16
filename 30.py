class Pessoas:
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

    def informacaoSaida(self):
        print(f"Olá, meu nome é", self.nome, self.sobrenome, "eu tenho", self.idade, "e moro em", self.cidade)

pessoa1= Pessoas(input('Nome'), input('Sobrenome'), input('Idade'), input('Cidade'))
pessoa2= Pessoas(input('Nome'), input('Sobrenome'), input('Idade'), input('Cidade'))
pessoa3= Pessoas(input('Nome'), input('Sobrenome'), input('Idade'), input('Cidade'))

pessoa1.informacaoSaida()
pessoa2.informacaoSaida()
pessoa3.informacaoSaida()