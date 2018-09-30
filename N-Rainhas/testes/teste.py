from random import randint

def geraPopulação(n):
    populacao=[]
    for x in range(0,n**4):
        populacao.append(criarIndividuo(n))
    return populacao

def criarIndividuo(n):
    individuo=[]
    for x in range(0,n):
        individuo.append(randint(1,n))
    return individuo

def funcaoObjetivo(lista):
    bin=[]
    for z in range(0,len(lista)):
        bin.append(1)
    for x in range (0,len(lista)):
        for y in range (x+1,len(lista)):
            if bin[y]!=0 and lista[x]==lista[y]:
                bin[x]=0
                bin[y]=0
            if bin[y]!=0 and ((x-y)**2)-((lista[x]-lista[y])**2)==0:
                bin[x]=0
                bin[y]=0

    y=0
    for x in range(0,len(bin)):
        if bin[x]==1:
            y=y+1
    return y

populacao=geraPopulação(5)
for x in range(0,len(populacao)):
    populacao[x]=[funcaoObjetivo(populacao[x]),populacao[x]]
