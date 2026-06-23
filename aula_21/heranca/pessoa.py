# Precisamos criar um molde de uma pessoa. => class
# Características -> atributos => variáveis. nome e cpf
# ações -> métodos => funções

class Pessoa: # Superclass porque oferece a herança
    # Constructor
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self.nome = nome # Atributo público
        self.cpf = cpf # Atributo privado
        self.data_nascimento = data_nascimento # Atributo público
    
    
    # Método de apresentação
    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}"
    

pessoa1 = Pessoa("Ana Lima", "123", "13/03/1992")
pessoa2 = Pessoa("Bruno Costa", "987", "17/05/2000")

print(pessoa1.apresentar())
print(pessoa2.apresentar())