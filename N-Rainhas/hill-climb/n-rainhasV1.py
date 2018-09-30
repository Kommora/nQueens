from random import randint
import timeit

def inicializaTabuleiro(n):
    tabuleiro=[]
    for x in range(0,n):
        tabuleiro.append(randint(1,n))
        # tabuleiro.append(1)
    return tabuleiro

def ataques(tab):
    custo=0
    for x in range(0,len(tab)):
        for y in range(x+1,len(tab)):
            if tab[x]==tab[y] or ((x-y)**2)-((tab[x]-tab[y])**2)==0:
                custo=custo+1
    return custo

def mover(tab,i,custo):
    # 1 moveu
    # 0 nao moveu
    # j=tab[i]
    # tab[i]=randint(1,len(tab))
    # custo_mover=ataques(tab)
    # if custo_mover<custo:
    #     return 1
    # else:
    #     tab[i]=j
    #     return 0
    if tab[i]==1:
        tab[i]=2
        custo_direita=ataques(tab)
        if custo_direita<custo:
            return 1
        if custo_direita==custo:
            if randint(0,1)==1:
                return 1
            else:
                tab[i] = 1
                return 0
        else:
            tab[i]=1
            return 0
    elif tab[i]==len(tab):
        tab[i]=len(tab)-1
        custo_esquerda=ataques(tab)
        if custo_esquerda<custo:
            return 1
        if custo_esquerda==custo:
            if randint(0, 1) == 1:
                return 1
            else:
                tab[i] = len(tab)
                return 0
        else:
            tab[i]=len(tab)
            return 0
    else:
        tab[i] = tab[i] - 1
        custo_esquerda=ataques(tab)
        tab[i]=tab[i]+2
        custo_direita=ataques(tab)
        if custo_esquerda<custo_direita and custo_esquerda<custo:
        # if custo_esquerda<custo:
            tab[i]=tab[i]-2
            return 1
        elif custo_direita<custo_esquerda and custo_direita<custo:
        # elif custo_direita < custo:
            return 1
        # elif custo_esquerda==custo_direita and custo_esquerda<custo:
        #     if randint(0,1)==1:
        #         return 1
        #     else:
        #         tab[i] = tab[i] - 2
        #         return 1
        elif custo_esquerda==custo:
            if randint(0,1)==1:
                tab[i] = tab[i] - 1
                return 0
            else:
                tab[i] = tab[i] - 2
                return 1
        elif custo_direita == custo:
            if randint(0, 1) == 1:
                return 1
            else:
                tab[i] = tab[i] - 1
                return 0
        else:
            tab[i]=tab[i]-1
        return 0

def modificar(tab):
    count=0
    while 1:
        i = randint(0, len(tab)-1)
        j=mover(tab,i,ataques(tab))
        # print(tab)
        if ataques(tab)==0:
            print("Solucao encontrada:"+str(tab))
            break
        if j==0:
            count=count+1
        else:
            count=0
        if count>=len(tab):
            # print("minimo local")
            tab=inicializaTabuleiro(len(tab))
            count=0
    return

# i=4
# while 1:
#     ini = timeit.default_timer()
#     tab=inicializaTabuleiro(i)
#     print("Tabuleiro inicial para "+str(i)+"-rainhas:"+str(tab))
#     modificar(tab)
#     print("Demorou:"+str(timeit.default_timer()-ini)+"\n")
#     i=i+1
modificar(inicializaTabuleiro(100))
# Tabuleiro inicial para 8-rainhas:[6, 4, 6, 5, 1, 2, 8, 8]