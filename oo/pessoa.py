class Pessoa:
  olhos = 2

  def __init__(self, *filhos, nome=None, idade=20):
    self.nome = nome
    self.idade = idade
    self.filhos = list(filhos)

  def cumprimentar(self):
    return f'olá {id(self)}'

  @staticmethod
  def metodo_estatico():
    return 42
  
  @classmethod
  def nome_e_atributos_de_classe(cls):
    return f'{cls} - olhos {cls.olhos}'

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
  print(Pessoa.metodo_estatico(), francisco.metodo_estatico())
  print(Pessoa.nome_e_atributos_de_classe(), francisco.nome_e_atributos_de_classe())
