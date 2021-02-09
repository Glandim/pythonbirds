class Pessoa:
  olhos = 2

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
  francisco.sobrenome = 'Landim'
  del francisco.filhos
  francisco.olhos = 1
  del francisco.olhos
  print(francisco.__dict__)
  print(gabriel.__dict__)
  Pessoa.olhos = 3
  print(Pessoa.olhos)
  print(francisco.olhos)
  print(gabriel.olhos)
  print(id(Pessoa.olhos), id(francisco.olhos), id(gabriel.olhos))
