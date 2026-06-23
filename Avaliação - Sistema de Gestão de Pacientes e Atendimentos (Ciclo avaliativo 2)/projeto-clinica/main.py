from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio

# Paciente Particular
paciente1 = PacienteParticular(
    "João Silva",
    "15/05/1990",
    "123.456.789-00",
    "(11) 99999-1111",
    "O+",
    "P001",
    "Pix",
    0.10
)

# Paciente Convênio
paciente2 = PacienteConvenio(
    "Maria Oliveira",
    "20/08/1985",
    "987.654.321-00",
    "(11) 98888-2222",
    "A+",
    "P002",
    "Unimed",
    "987654321"
)

print("=== PACIENTE PARTICULAR ===")
paciente1.exibir_informacoes(True)

valor = paciente1.calcular_valor_final(
    valor_consulta=200,
    taxa_urgencia=50
)

print(f"Valor final: R$ {valor:.2f}")

paciente1.registrar_atendimento(
    "Consulta Cardiológica",
    valor
)

print("\n========================\n")

print("=== PACIENTE CONVÊNIO ===")
paciente2.exibir_informacoes(True)

paciente2.registrar_autorizacao(
    "Ressonância Magnética",
    50
)

paciente2.registrar_atendimento(
    "Ressonância Magnética",
    0
)