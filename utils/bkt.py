

def init(n):
    
    V=[-1]*n
    return  V


def satisf(W,V,k,cond):
    
    if V[k-1]>V[k]:
        return 0
    
    for i in range(0,k):
        if cond(W[V[i]],W[V[k]]):
            return  0
        
    return 1

def sol(q,k):
    return k==q-1

def print_sol(V,W,n):

    for i in range(0,n):
        print(W[V[i]],end='|||')
        
    print('\n')

def Bkt(W,q,cond):
    k=0
    n=len(W)
    V=init(q)
    
    while k>=0:
        while V[k]<n-1:
            
            V[k]+=1
            
            if satisf(W,V,k,cond):
                if sol(q,k):
                    print_sol(V,W,q)
                else:
                    k+=1
                    
        V[k]=-1
        k-=1
            
            
    
    
    
    
    
