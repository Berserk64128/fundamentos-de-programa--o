from pessoa import Pessoa
# NOME, CPF, DATA DE NASCIMENTP, ANO DE INGRESSO, NOTAS, MATRICULA E SE ESTAR ATIVO OU NÃO
class Aluno(Pessoa): # Subclass porque recebe a herança
    def __init__(self, nome: str, cpf: str, data_nascimento: str, ano_ingresso: int, matricula: str):
        super().__init__(nome, cpf, data_nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self.ativo = True
        self.notas = []

    # Método de notas
    def adicionar_notas(self, disciplina: str, nota: float):
    # nota esteja entre 0 e 10
        if nota(0 <= nota <=10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        
        if disciplina not in self.notas:
            self.notas[disciplina] = []

        self.notas[disciplina].append(nota)