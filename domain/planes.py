


class Plane():
    
    #constructor
    def __init__(self,n='',nr=0,arc='',nrs=0,dest='',lps=[]):
        
        self.__name=n
        self.__number=nr
        self.__airline_company=arc
        self.__number_seats=nrs
        self.__destination=dest
        self.__list_passengers=lps[:]
    
    #setter    
    def set_name(self,n):
        self.__name=n
        
    #setter    
    def set_number(self,nr):
        self.__number=nr
        
    #setter    
    def set_airline_company(self,arc):
        self.__airline_company=arc
        
    #setter    
    def set_number_seats(self,nrs):
        self.__number_seats=nrs
        
    #setter    
    def set_destination(self,dest):
        self.__destination=dest
        
    #setter    
    def set_list_passengers(self,lps):
        self.__list_passengers=lps
        
    #getter    
    def get_name(self):
        return  self.__name
    
    #getter
    def get_number(self):
        return self.__number
    
    #getter
    def get_airline_company(self):
        return self.__airline_company
    
    #getter
    def get_number_seats(self):
        return self.__number_seats
    
    #getter
    def get_destination(self):
        return self.__destination
    
    #getter
    def get_list_passengers(self):
        return self.__list_passengers
    
    
    
    def add_passenger(self,passenger):
        
        """
            input: -
            output: A modified Plane.
            desc.: Add a Passenger to the list of passengers. 
        """
        self.__list_passengers.append(passenger)
    
    def __str__(self):
        return "Name:" + self.__name +" --- "+"Number: "+ str(self.__number) +" --- "+"Airline Company:"+ self.__airline_company +" --- "+"Number of seats:"+ str(self.__number_seats)+" --- "+'Destination:'+self.__destination +" --- "+"List of passengers:"+ str(self.__list_passengers)
    
    def __repr__(self):
        return str(self)
        
        