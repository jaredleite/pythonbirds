class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'
    pass


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(id(p))