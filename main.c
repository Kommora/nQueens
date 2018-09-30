#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int ini(int n,int tab[]){
    for(int i=0;i< n;i++){
        tab[i]=i+1;
    }
    return 0;
}

void ini2(int n,int tab[]){
//    int i=1,j=2;
//    tab[0]=1;

    if(n%2!=0){
        for(int i=0;i<=(n/2);i++){
            if(i==0){
                tab[0]=i+1;
            } else{
                tab[i]=tab[i-1]+2;
            }
        }
        tab[(n/2)+1]=2;
        for(int i=((n/2)+2);i<n;i++){
            tab[i]=tab[i-1]+2;
        }
    } else{
        for(int i=0;i<(n/2);i++){
            if(i==0){
                tab[i]=i+1;
            } else{
                tab[i]=tab[i-1]+2;
            }
        }
        tab[(n/2)]=2;
        for(int i=((n/2)+1);i<n;i++){
            tab[i]=tab[i-1]+2;
        }
    }

//
//
//    for(int i=0;i<n;i++){
//        printf("%d ",tab[i]);
//    }
}

int atkBoard(int n,int tab[]){
    int cost=0;
    for(int x=0;x<n;x++){
        for (int y=x+1;y<n;y++){
            if(tab[x]==tab[y] || (abs(x-y)-abs(tab[x]-tab[y]))==0){
                cost++;
            }
        }
    }
    return cost;
}

int atkQueen(int n,int y,int tab[]){
    int cost=0;
    for(int x=0;x<n;x++){
        if(x!=y && tab[x]==tab[y] || (abs(x-y)-abs(tab[x]-tab[y]))==0){
            cost++;
        }

    }
    return cost;
}

void mover(int n,int tab[]){
    int old_cost=atkBoard(n,tab);
    while (1){

        if(old_cost==0){
            break;
        }
        int new_line=rand()%n;
        int new_line2=rand()%n;

        int aux = tab[new_line];

        tab[new_line]=tab[new_line2];
        tab[new_line2]=aux;


        int new_cost=atkBoard(n,tab);

        if (new_cost==0){
            break;
        }
        if(new_cost>old_cost){
            tab[new_line2]=tab[new_line];
            tab[new_line]=aux;
        } else{
            old_cost=new_cost;
        }
    }
    printf("achou\n");
}

int most(){

}

void print(int n,int tab[]){
    for(int i=0;i<n;i++){
        printf("%d ",tab[i]);
    }
    printf("\n");
}

void toString(int n,int tab[], double tempo){
    FILE *t = fopen("n-rainhas.txt","a+");
    fprintf(t,"%d\n%f\n",n,tempo);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if((j+1)==tab[i]){
                fprintf(t,"1 ");
            } else{
                fprintf(t,"0 ");
            }
        }
        fprintf(t,"\n");
    }
    fclose(t);
}
int main(){
    int n=1000;
    int tab[n];
//    ini(n,tab);
//    printf("%d",atkBoard(n,tab));
    ini2(n,tab);
    clock_t t;
    t = clock();
    mover(n,tab);
    t = clock()-t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    toString(n,tab,time_taken);
    print(n,tab);
//    return 0;
}
