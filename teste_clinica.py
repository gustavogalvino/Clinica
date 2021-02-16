from clinica import Clinica, Funcionario, Medico, Paciente, Quarto, Historico

# Criação Clínica
clinica = Clinica("Clínica Médica", "Rua Capitão João Pompeo, 422")

# Criação Funcionários
camila = Funcionario("Camila Moreira", "513.285.584-95", "35.448.998-7",
                     "(11) 98245-1754", 1500)
fernanda = Medico("Fernanda Gomes", "317.355.128-18", "17.523.404-8",
                  "(11) 98676-4208", 3000, "14885077-8/BR")
martin = Medico("Martin Thales", "936.349.978-26", "31.143.346-7",
                "(11) 98235-9445", 3000, "60065032-5/BR")

# Criaçao Paciente
rafaela = Paciente("Rafaela Novaes", "601.732.398-97", "24.471.273-6",
                   "(11) 99585-6183", "Rua Uruaçu, 610", "16/05/1989")
leandro = Paciente("Leandro Figueiredo", "440.329.018-30", "39.784.013-5",
                   "(11) 98570-0032", "Rua Bilimbi, 944", "21/08/2010")

# Criação dos Quartos
quarto1 = Quarto(2, 236)
quarto2 = Quarto(3, 321)
quarto3 = Quarto(2, 202)

# incluindo Especialidades
fernanda.incluir_especialidade("Cardiologia")
fernanda.incluir_especialidade("Infectologia")
fernanda.incluir_especialidade("Neurologia")
martin.incluir_especialidade("Pediatria")
martin.incluir_especialidade("Dermatologia")

# Incluindo Funcionários
clinica.incluir_funcionarios("Fernanda Gomes", "Cardiologia")
clinica.incluir_funcionarios("Martin Thales", "Pediatria")
clinica.incluir_funcionarios("Camila Moreira", "Atendente")

# Definindo Convênio
rafaela.set_num_convenio("6142695160")

# Definindo Responsabilidade
rafaela.set_responsavel("Fernanda Gomes")
leandro.set_responsavel("Martin Thales")

# Adicionando aos Quartos
quarto1.set_paciente("rafaela")
quarto3.set_paciente("leandro")

# Criando Histórico
observacao1 = "Paciente Estável."
observacao2 = "Paciente em Recuperação."
historico1 = Historico("29/10/2020", "18:18", observacao1,
                       fernanda.get_assinatura())
historico1.adiciona_observacao()
historico2 = Historico("21/01/2020", "22:10", observacao2,
                       martin.get_assinatura())
historico2.adiciona_observacao()

# Adicionando Histórico
rafaela.adiciona_historico(historico1.get_lista())
leandro.adiciona_historico(historico2.get_lista())

# Exibindo Funcionários
print(30 * "-")
print("Funcionários:")
print()
clinica.exibir_funcionarios()
print()

# Exibindo Informações Funcionários
print(30 * "-")
print("Informações Funcionários:")
print()
camila.informacoes()
fernanda.informacoes()
martin.informacoes()
print()

# Exibindo Informações Pacientes
print(30 * "-")
print("Informações Pacientes:")
print()
rafaela.informacoes()
leandro.informacoes()
print()

# Assinaturas
print(30 * "-")
print("Assinaturas Funcionários:")
print()
camila.assinatura()
print()
fernanda.assinatura()
print()
martin.assinatura()
print()
print(30 * "-")
print("Assinaturas Pacientes:")
print()
rafaela.assinatura()
print()
leandro.assinatura()
print()

# Exibindo Históricos
print(30 * "-")
print("Chaves de buasca pelo histórico:")
print()
rafaela.exibe_chaves()
print()
leandro.exibe_chaves()

print(30 * "-")
print("Busca parcial:")
print()
rafaela.exibe_historico("29/10/2020 - 18:18")
print()
leandro.exibe_historico("21/01/2020 - 22:10")

print(30 * "-")
print("Busca total:")
print()
rafaela.historico_completo()
print()
leandro.historico_completo()
