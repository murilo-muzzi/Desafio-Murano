# Desafio PS Murano Investimentos
# Candidato: Murilo Marinho Muzzi Ribeiro
# e-mail: murilomarinhomuzzi@gmail.com

# Questões de computação e programação
# Feito em Python

# 5)
print ('Funções de ordenação')
print ('Lista de exemplo: [194,57,1,9,66,47,89,200]')
print ('Merge Sort:')

# Merge Sort

def MergeSort (lista):
    print ("Dividindo ",lista)
    if len(lista)>1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        MergeSort(esquerda)
        MergeSort(direita)

        i=0
        j=0
        k=0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i = i + 1
            else:
                lista[k] = direita[j]
                j = j + 1
            k = k + 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i = i + 1
            k = k + 1

        while j < len(direita):
            listak = direita[j]
            j = j + 1
            k = k + 1

    print ("Juntando ",lista)


lista_exemplo = [194,57,1,9,66,47,89,200]
MergeSort(lista_exemplo)
print(lista_exemplo)

print ('Quick Sort:')

# Quick Sort

def QuickSort(lista):
    QuickSortHelper(lista,0,len(lista)-1)

def QuickSortHelper(lista,primeiro,ultimo):
    if primeiro < ultimo:
        
        splitpoint = particao(lista,primeiro,ultimo)
        
        QuickSortHelper(lista,primeiro,splitpoint-1)
        QuickSortHelper(lista,splitpoint+1,ultimo)

def particao(lista,primeiro,ultimo):
    pivotvalue = lista[primeiro]
    
    esquerda = primeiro + 1
    direita = ultimo
    
    done = False
    while not done:
        
        while esquerda <= direita and lista[esquerda] <= pivotvalue:
            esquerda = esquerda + 1
            
        while direita >= esquerda and lista[direita] >= pivotvalue:
            direita = direita - 1
            
        if direita < esquerda:
            done = True
        else:
            temp = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = temp
            
    temp = lista[primeiro]
    lista[primeiro] = lista[direita]
    lista[direita] = temp
    
    return direita


lista_exemplo = [194,57,1,9,66,47,89,200]
QuickSort(lista_exemplo)
print(lista_exemplo)

print ('Bubble Sort:')

# Bubble Sort

def BubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp


lista_exemplo = [194,57,1,9,66,47,89,200]
BubbleSort(lista_exemplo)
print(lista_exemplo)



# 6
print ('Iniciando calculadora de investimento')

def deposito(idade_atual,idade_final,valor_futuro,juros):
    n = (idade_final - idade_atual)*12
    i = juros/100

    valor_mensal = round((valor_futuro * i)/(((1 + i)**n) - 1),2)

    print ('É necessário aportar R$',valor_mensal,' por mês')

idade_atual = float(input('Quantos anos você tem? '))
idade_final = float(input('Com quantos anos deseja retirar o dinheiro aplicado? '))
valor_futuro = float(input('Qual a quantia desejada no final do período? '))
juros = float(input('Qual a taxa de juros fixa mensal esperada? '))
deposito(idade_atual,idade_final,valor_futuro,juros)


