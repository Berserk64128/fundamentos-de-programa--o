from paciente import Paciente

class PacienteParticular(Paciente):

    def __init__(self, nome, data_nascimento, cpf,
                 telefone, tipo_sanguineo, numero_prontuario,
                 forma_pagamento, desconto_fidelidade):

        super().__init__(
            nome,
            data_nascimento,
            cpf,
            telefone,
            tipo_sanguineo,
            numero_prontuario
        )

        self._forma_pagamento = forma_pagamento
        self._desconto_fidelidade = desconto_fidelidade

    def calcular_valor_final(self, valor_consulta, taxa_urgencia):

        valor = valor_consulta + taxa_urgencia

        desconto = valor_consulta * self._desconto_fidelidade

        valor_final = valor - desconto

        return valor_final

    def exibir_informacoes(self, detalhado=False):

        super().exibir_informacoes(detalhado)

        print(f"Forma de pagamento: {self._forma_pagamento}")
        print(
            f"Desconto fidelidade: {self._desconto_fidelidade * 100:.0f}%"
        )