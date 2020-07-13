# Desafio PS Murano Investimentos
# Candidato: Murilo Marinho Muzzi Ribeiro
# e-mail: murilomarinhomuzzi@gmail.com

# Questões de computação e programação
# Feito em Python

# 7)

continuar = 'sim'
while continuar == 'sim':
    dados = dict()

    dados['dre'] = int(input('Digite o DRE: '))

    dados['curso'] = input('Digite o Curso: ')

    dados['nome'] = input('Digite o nome do(a) aluno(a): ')

    while True:
        dados['genero'] = input('Digite o gênero: [M] ou [F] ')
        if dados['genero'] == 'M' or dados['genero'] == 'F':
            break
        
    dados['data_nascimento'] = input('Digite a data de nascimento: ')

    dados['altura'] = (input('Digite a altura do(a) aluno(a): '))
        
    dados['peso'] = (input('Digite o peso do(a) aluno(a): '))
        
    dados['cra'] = (input('Digite o CR acumulado do(a) aluno(a): '))
    dados['cra'] = dados['cra'].replace(",",".")
    dados['cra'] = float(dados['cra'])
    while dados['cra'] < 0 or dados['cra'] > 10:
        dados['cra'] = float(input('Digite novamente o CR acumulado do(a) aluno(a): '))
        
    dados['creditos'] = int(input('Digite a quantidade de créditos obtidos do(a) aluno(a): '))
    while dados['creditos'] <= 0:
        dados['creditos'] = int(input('Digite novamente a quantidade de créditos obtidos do(a) aluno(a): '))
        
    dados['renda'] = (input('Digite a renda do(a) aluno(a): '))
    dados['renda'] = dados['renda'].replace(",",".")
    dados['renda'] = float(dados['renda'])
    while dados['renda'] < 0:
        dados['renda'] = float(input('Digite novamente a renda do(a) aluno(a): '))

    with open('dados.txt','a') as arquivo:
        for valor in dados.items():
            arquivo.write(str(valor)+'\n')

    continuar = input('Deseja continuar? [sim] ou [nao] ')
