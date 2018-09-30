from random import randint
import timeit

def inicializaTabuleiro(n):
    tabuleiro=[]
    for x in range(0,n):
        tabuleiro.append(x+1)
    return tabuleiro

def ataques(tab):
    custo=0
    for x in range(0,len(tab)):
        for y in range(x+1,len(tab)):
            if tab[x]==tab[y] or (abs(x-y)-abs(tab[x]-tab[y]))==0:
                custo=custo+1
    return custo

def mover(tab):
    reinicio=0
    while 1:
        custo_atual=ataques(tab)
        if custo_atual==0:
            break
        novo_linha=randint(0,len(tab)-1)
        novo_coluna=randint(1,len(tab))
        velho_coluna=tab[novo_linha]
        tab[novo_linha]=novo_coluna
        custo_novo=ataques(tab)
        if custo_novo == 0:
            break
        if custo_novo>custo_atual:
            tab[novo_linha]=velho_coluna
            print(custo_atual)
        # elif custo_atual==custo_novo:
        #     if randint(0,1)==1:
        #         tab[novo_linha] = velho_coluna
        #         print(custo_atual)
        #     else:
        #         print(custo_novo)
        else:
            print(custo_novo)
    print("achou")
    print(tab)
    return

ini = timeit.default_timer()
mover(inicializaTabuleiro(500))
print("Demorou:"+str(timeit.default_timer()-ini)+"\n")