class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'
    pass


if __name__ == '__main__':
    p = Pessoa('Jared')
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)