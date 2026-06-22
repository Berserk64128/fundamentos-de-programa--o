from paciente import Paciente

class PacienteConvenio(Paciente):

    def __init__(self, nome, data_nascimento, cpf,
                 telefone, tipo_sanguineo, numero_prontuario,
                 nome_convenio, numero_carteirinha):

        super().__init__(
            nome,
            data_nascimento,
            cpf,
            telefone,
            tipo_sanguineo,
            numero_prontuario
        )

        self._nome_convenio = nome_convenio
        self._numero_carteirinha = numero_carteirinha

    def registrar_autorizacao(self, procedimento, valor_glosa):

        print(f"Procedimento autorizado: {procedimento}")
        print(f"Valor da glosa: R$ {valor_glosa:.2f}")

    def exibir_informacoes(self, detalhado=False):

        super().exibir_informacoes(detalhado)

        print(f"Convênio: {self._nome_convenio}")
        print(f"Carteirinha: {self._numero_carteirinha}")