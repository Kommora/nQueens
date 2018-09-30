from random import randint
import timeit


def init(n):
    tab=[]
    for x in range(0,n):
        tab.append(0)
    return tab

def set(tab):
    i=0
    j=1
    while 1:
        print(tab)
        if i==len(tab):
            i=0
        if ataques(tab)==0:
            return tab
        if atk(tab,i)==0:
            i=i+1
        else:
            tab=init(len(tab))
            i=1
            j=j+1
            if j<=len(tab):
                tab[0] = j
    return tab

def atk(tab,i):
    tab[i]=tab[i]+1
    if tab[i]>len(tab):
        tab[i]=0
        return 1
    x=0
    while x<i:
        if randint(1,100)>60 and x!=i and tab[x]!=0 and (tab[x]==tab[i] or (((x-i)**2)-((tab[x]-tab[i])**2)==0)):
            tab[i]=tab[i]+1
            if tab[i]>len(tab):
                tab[i]=0
                return 1
            else:
                x=0
        else:
            x=x+1

    return 0

def ataques(tab):
    custo=0
    for x in range(0,len(tab)):
        for y in range(x+1,len(tab)):
            if tab[x]==tab[y] or ((x-y)**2)-((tab[x]-tab[y])**2)==0:
                custo=custo+1
    return custo


ini = timeit.default_timer()
print(set(init(4)))
print("Demorou:" + str(timeit.default_timer() - ini) + "\n")