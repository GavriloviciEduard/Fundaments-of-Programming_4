

class Passenger():
    

    #constructor
    def __init__(self,fn='',ln='',nrp=0):
        
        self.__first_name=fn
        self.__last_name=ln
        self.__passport_number=nrp
        
    #setter
    def set_first_name(self,fn):
        self.__first_name=fn
        
    #setter    
    def set_last_name(self,ln):
        self.__last_name=ln
    
    #setter    
    def set_passport_number(self,nrp):
        self.__passport_number=nrp
    
    #getter    
    def get_first_name(self):
        return self.__first_name
    
    #getter
    def get_last_name(self):
        return self.__last_name
    
    #getter
    def get_passport_number(self):
        return self.__passport_number
    
    def __str__(self):
        return "First name:"+ self.__first_name+" --- "+"Last name:"+ self.__last_name+" --- "+"Passport number:"+str(self.__passport_number)
    
    def __repr__(self):
        return str(self)
        
        
        