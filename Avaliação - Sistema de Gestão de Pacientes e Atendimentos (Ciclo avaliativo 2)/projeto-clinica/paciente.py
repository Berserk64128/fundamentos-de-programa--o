class Paciente:
    def __init__(self, nome, data_nascimento, cpf,
                 telefone, tipo_sanguineo, numero_prontuario):

        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self._tipo_sanguineo = tipo_sanguineo
        self._numero_prontuario = numero_prontuario

    def registrar_atendimento(self, tipo, custo):
        print(f"Paciente {self._nome} realizou um atendimento do tipo {tipo}.")
        print(f"Custo do atendimento: R$ {custo:.2f}")

    def exibir_informacoes(self, detalhado=False):

        if detalhado:
            print(f"Nome: {self._nome}")
            print(f"Data de nascimento: {self._data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self._telefone}")
            print(f"Tipo sanguíneo: {self._tipo_sanguineo}")
            print(f"Prontuário: {self._numero_prontuario}")
        else:
            print(f"Nome: {self._nome}")
            print(f"Prontuário: {self._numero_prontuario}")
            print(f"Tipo sanguíneo: {self._tipo_sanguineo}")