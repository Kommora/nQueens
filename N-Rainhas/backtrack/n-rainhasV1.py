import timeit
from random import randint

def init(n):
    tab=[]
    for x in range(0,n):
        tab.append(0)
    return tab


def set(tab):
    i=1
    tab[0] = randint(1,len(tab))
    while i<len(tab):
        print(tab)
        if atk(tab,i)==0:
            i=i+1
        else:
            i=i-1
    return tab

def atk(tab,i):
    tab[i]=tab[i]+1
    if tab[i]>len(tab):
        tab[i]=0
        return 1
    x=0
    while x<i:
        if x!=i and tab[x]!=0 and (tab[x]==tab[i] or (((x-i)**2)-((tab[x]-tab[i])**2)==0)):
            tab[i]=tab[i]+1
            if tab[i]>len(tab):
                tab[i]=0
                return 1
            else:
                x=0
        else:
            x=x+1
    return 0

ini = timeit.default_timer()
print(set(init(100)))
print("Demorou:" + str(timeit.default_timer() - ini) + "\n")