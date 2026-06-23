# Sistema de Gestão de Pacientes e Atendimentos

Feito por: Arthur Seabra de Mesquita.

## Descrição

Sistema desenvolvido em Python utilizando Programação Orientada a Objetos para gerenciar pacientes de uma clínica médica.

Foram utilizados os conceitos de:

- Herança
- Encapsulamento
- Polimorfismo
- Sobrescrita de métodos

## Classes

### Paciente

Classe base contendo os dados comuns a todos os pacientes.

### PacienteParticular

Herda de Paciente e adiciona informações de pagamento e desconto de fidelidade.

### PacienteConvenio

Herda de Paciente e adiciona informações referentes ao plano de saúde.

## Exemplo de execução

```text
=== PACIENTE PARTICULAR ===
Nome: João Silva
Data de nascimento: 15/05/1990
CPF: 123.456.789-00
Telefone: (11) 99999-1111
Tipo sanguíneo: O+
Prontuário: P001
Forma de pagamento: Pix
Desconto fidelidade: 10%
Valor final: R$ 230.00
```