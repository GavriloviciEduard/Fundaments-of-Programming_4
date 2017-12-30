

class PassengersRepo():
    
    #constructor
    def __init__(self):
        
        self.__repo=[]
        
    def add_passenger(self,obj):
        
        """
            input: A Passenger.
            output: A modified repository.
            desc.: The method adds a new passenger in the repository. 
        """
        self.__repo.append(obj)
        
    def get_all_passengers(self):
        
        """
            input: -
            output: A repository.
            desc.: The method returns all the values from the repository.
        """
        return self.__repo
    
    def clear_repo_ps(self):
        
        """
            input: -
            output: A modified repository.
            desc.: The method deletes all the values from the repository.
        """
        
        self.__repo=[]
        
    def del_passenger(self,i):
        
        """
            input: An index.
            output: A modified repository.
            desc.: The method deletes the values from the repository for a given index.
        """
        
        if len(self.__repo)>i: 
            del(self.__repo[i])
        
    def up_passenger(self,i,obj):
        
        """
            input: An index.
            output: A modified repository.
            desc.: The method updates the values from the repository for a given index.
        """
        
        if len(self.__repo)>i: 
            self.__repo[i]=obj
            
            
    def __len__(self):
        return len(self.__repo)
    
    
        
        
    def __str__(self):
        s=""
        
        for el in self.__repo:
            s+=str(el)+"\n"
            
        return s