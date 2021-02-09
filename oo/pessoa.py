class Pessoa:
  def __init__(self, *filhos, nome=None, idade=20):
    self.nome = nome
    self.idade = idade
    self.filhos = list(filhos)

  def cumprimentar(self):
    return f'olá {id(self)}'

if __name__ == '__main__':
  gabriel = Pessoa(nome='Gabriel')
  landim = Pessoa(gabriel, nome='Landim')
  print(Pessoa.cumprimentar(landim))
  print(id(landim))
  print(landim.cumprimentar())
  print(landim.nome)
  print(landim.idade)
  for filho in landim.filhos:
    print(filho.nome)
