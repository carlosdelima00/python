def classe():
    class Pessoa():  #poo sem o metodo construtor '__init__' 
        nome = "carlos"
        idade = 17
        cidade = "iguatu"
        estudante = True

class Humano(): #poo com o metodo '__init__'
    def __init__(self,nome,idade,cidade,grau_estudo):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.grau_estudo = grau_estudo

lista_de_pessoas = 0

pessoa1 = Humano("carlos",17,"iguatu","fundamental completo")
pessoa2 = Humano("paulo",34,"rio de janeiro","graduado")
pessoa3 = Humano("jonas",67,"juazeiro","analfabeto")


print(pessoa1.nome.__len__())
print(pessoa2.nome.__len__())
print(pessoa3.nome.__len__())

soma_de_nomes = pessoa1.nome.__len__() + pessoa2.nome.__len__()
print(soma_de_nomes)
        
    
