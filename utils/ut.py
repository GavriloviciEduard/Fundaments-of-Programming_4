
def equal_pass(a,b):
    return a.get_passport_number()==b
def equal_plane(a,b):
    return a.get_number()==b    
def asc(a,b):
    return a.get_last_name()>b.get_last_name()
    
def desc(a,b):
    return a.get_last_name()<b.get_last_name()
    
def comp_x_asc(obj_1,obj_2,x):
    i,j=0,0
    
   
    l1=obj_1.get_list_passengers()
    l2=obj_2.get_list_passengers()
    
    for el in l1:
        name=el.get_first_name()
        if name[0]==x:
            i+=1
            
    for el in l2:
        name=el.get_first_name()
        if name[0]==x:
            j+=1
            
    return i>j

def comp_x_desc(obj_1,obj_2,x):
    i,j=0,0
    
    
    
    l1=obj_1.get_list_passengers()
    l2=obj_2.get_list_passengers()
    
    for el in l1:
        name=el.get_first_name()
        if name[0]==x:
            i+=1
            
    for el in l2:
        name=el.get_first_name()
        if name[0]==x:
            j+=1
            
    return i<j

def comp_conc_asc(obj_1,obj_2):
    
    a=str(len(obj_1.get_list_passengers())) + str(obj_1.get_number())
    b=str(len(obj_2.get_list_passengers())) + str(obj_2.get_number())
    
    return a>b

def comp_conc_desc(obj_1,obj_2):
    
    a=str(len(obj_1.get_list_passengers())) + str(obj_1.get_number())
    b=str(len(obj_2.get_list_passengers())) + str(obj_2.get_number())
    
    return a<b

def thr_pp(obj,b):
    
    
    
    obj=obj.get_passport_number()
    obj=str(obj)
    obj=str(obj[0])+str(obj[1])+str(obj[2])
        
    return obj==b

def eq(a,b):
    
    b=b.lower()
    
    if b in a.get_first_name():
        return 1
    
    if b.upper() in a.get_first_name():
        return 1
    
    if b in a.get_last_name():
        return 1
    
    if b.upper() in a.get_last_name():
        return 1
    
    
    
    
    
    return 0
    
def pl_eq(a,b):
    
    if a.get_name()==b:
        return 1
    
    return 0

def eq_name(a,b):
    
    a=a.get_list_passengers()
    
    for el in a :
        
        s=el.get_first_name() +" " +el.get_last_name()
        
        if s==b:
            return 1
        
    return 0

def eq_nrpass(a,b):
    
    if a.get_passport_number()==b:
        return 1
    
    return 0

def ls_eq(a,b):
    
    if a.get_last_name()==b.get_last_name():
        return 1
    return 0

def ac_eq(a,b):
    
    return a.get_airline_company()==b.get_airline_company()
        
    
    
    
    
    
