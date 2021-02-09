class Pessoa:
  def __init__(self, nome=None, idade=20):
    self.nome = nome
    self.idade = idade

  def cumprimentar(self):
    return f'olá {id(self)}'

if __name__ == '__main__':
  p = Pessoa('Gabriel')
  print(Pessoa.cumprimentar(p))
  print(id(p))
  print(p.cumprimentar())
  print(p.nome)
  p.nome = 'Landim'
  print(p.nome)
  print(p.idade)
