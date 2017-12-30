

def search(lst,s,met):
    
    for el in lst:
        if met(el,s):
            return 0
        
    return 1

def my_sort(lst,cond,x=' '):
    
   
    
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if x==' ':
                if cond(lst[i],lst[j]):
                    lst[i],lst[j]=lst[j],lst[i]
            else:
                if cond(lst[i],lst[j],x):
                    lst[i],lst[j]=lst[j],lst[i]
                
                
    return lst

def my_filter(lst,cond,x=' '):
    
    r=[]
    
    
    if x==' ':
        x=lst[0].get_passport_number()
        x=str(x)
        x=str(x[0])+str(x[1])+str(x[2])
        
    
        for i in range(1,len(lst)):
        
            if cond(lst[i],x):
                r.append(lst[i])
            
        return r
    
    else:
        for i in range(0,len(lst)):
        
            if cond(lst[i],x):
                r.append(lst[i])
            
        return r

    
            