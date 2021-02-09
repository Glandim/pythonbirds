class Pessoa:
  def __init__(self, *filhos, nome=None, idade=20):
    self.nome = nome
    self.idade = idade
    self.filhos = list(filhos)

  def cumprimentar(self):
    return f'olá {id(self)}'

if __name__ == '__main__':
  gabriel = Pessoa(nome='Gabriel')
  francisco = Pessoa(gabriel, nome='Francisco')
  print(Pessoa.cumprimentar(francisco))
  print(id(francisco))
  print(francisco.cumprimentar())
  print(francisco.nome)
  print(francisco.idade)
  for filho in francisco.filhos:
    print(filho.nome)
