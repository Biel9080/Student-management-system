# Exibe uma mensagem de boas-vindas ao iniciar o programa
print("Bússola.IpêAmarelo.com")
print("=" * 40)
print("BEM-VINDO À ESCOLA CLASSE IPÊ AMARELO")
print("ENSINO FUNDAMENTAL II")
print("=" * 40)


# Função responsável por cadastrar os dados do aluno
def cadastrar_dados():
    nome = input('Nome do aluno: ')


    # Lista fixa de disciplinas corrigida (incluindo Geografia)
    disciplinas_nomes = [
        'Português',
        'Matemática',
        'Ciências',
        'História',
        'Geografia'
    ]


    disciplinas = []


    # Percorre cada disciplina da lista
    for nome_materia in disciplinas_nomes:
        print(f"\n--- {nome_materia.upper()} ---")
       
        soma_notas_bimestres = 0
        # Solicita a nota dos 4 bimestres exigidos na lista
        for b in range(1, 5):
            while True:
                nota = float(input(f'Digite a nota do {b}º Bimestre: '))
                if 0 <= nota <= 10:
                    soma_notas_bimestres += nota
                    break
                else:
                    print("Erro! A nota deve estar entre 0 e 10. Tente novamente.")


        # Calcula a média daquela matéria específica
        media_materia = soma_notas_bimestres / 4


        # Validação das faltas (totais da matéria no ano)
        while True:
            faltas = int(input(f'Digite a quantidade TOTAL de faltas em {nome_materia}: '))
            if faltas >= 0:
                break
            else:
                print("Erro! O número de faltas não pode ser negativo.")


        # Armazena os dados processados da disciplina
        dados_materia = {
            'nome': nome_materia,
            'media': media_materia,
            'faltas': faltas
        }


        disciplinas.append(dados_materia)


    return nome, disciplinas




# Função que calcula a média geral de todas as matérias
def calcular_nota_geral(disciplinas):
    soma_medias = sum(d['media'] for d in disciplinas)
    media_geral = soma_medias / len(disciplinas)
    return media_geral




# Função que calcula o total de faltas acumuladas
def calcular_frequencia(disciplinas):
    total_faltas = sum(d['faltas'] for d in disciplinas)
    return total_faltas




# Função responsável por exibir o relatório final
def gerar_relatorio_final(nome, disciplinas, media_geral, total_faltas):
    print("\n" + "=" * 40)
    print("ESCOLA CLASSE IPÊ AMARELO")
    print("ENSINO FUNDAMENTAL II")
    print("=" * 40)
    print(f"RELATÓRIO FINAL DO ALUNO: {nome.upper()}")
    print("=" * 40)
    print("DETALHAMENTO POR DISCIPLINA:")


    # Percorre cada disciplina para exibir seus dados baseados na média dos 4 bimestres
    for d in disciplinas:
        status_materia = (
            "Aprovado" if d['media'] >= 7.0
            else "Recuperação" if d['media'] >= 5.0
            else "Reprovado"
        )
        print(f"- {d['nome']}: Média Final: {d['media']:.1f} | Faltas: {d['faltas']} ({status_materia})")


    print("-" * 40)
    print(f"Média Geral do Aluno: {media_geral:.2f}")
    print(f"Total de Faltas no Ano: {total_faltas} (Máximo permitido: 25)")
    print("-" * 40)


    # Mudamos a média para 7.0 (Antes 5.0)
    # Verifica a situação final do aluno (Média 7.0 para aprovação, limite de 25 faltas)
    if total_faltas > 25:
        print("STATUS FINAL: REPROVADO POR FALTAS")
    elif media_geral >= 7.0:
        print("STATUS FINAL: APROVADO")
    elif media_geral >= 5.0:
        print("STATUS FINAL: RECUPERAÇÃO")
    else:
        print("STATUS FINAL: REPROVADO POR NOTA")


    print("=" * 40)




# Execução do programa
nome_aluno, lista_disciplinas = cadastrar_dados()
media_final = calcular_nota_geral(lista_disciplinas)
faltas_acumuladas = calcular_frequencia(lista_disciplinas)
gerar_relatorio_final(nome_aluno, lista_disciplinas, media_final, faltas_acumuladas)