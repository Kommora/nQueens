import timeit
from random import randint,uniform

def init(n):
    tab=[]
    for x in range(0,n):
        tab.append(x+1)
    return tab


def set(tab):
    temperatura_ini=100.0
    temperatura=35.0
    while True:
        linha1=randint(0,len(tab)-1)
        linha2=randint(0,len(tab)-1)
        if linha1!=linha2:
            custo=ataques(tab)
            aux=tab[linha1]
            tab[linha1]=tab[linha2]
            tab[linha2]=aux
            custo_novo=ataques(tab)
            # print(tab)
            # print(temperatura)
            if ataques(tab)==0:
                print("achou")
                break
            if custo_novo>=custo:
                if not(round(uniform(0, temperatura_ini),3) < temperatura):
                    aux = tab[linha2]
                    tab[linha2] = tab[linha1]
                    tab[linha1] = aux
            if temperatura>0.0:
                temperatura=round(temperatura-0.001,3)

    return tab

def ataques(tab):
    custo=0
    for x in range(0,len(tab)):
        for y in range(x+1,len(tab)):
            if tab[x]==tab[y] or ((x-y)**2)-((tab[x]-tab[y])**2)==0:
                custo=custo+1
    return custo

ini = timeit.default_timer()
print(set(init(500)))
print("Demorou:" + str(timeit.default_timer() - ini) + "\n")
