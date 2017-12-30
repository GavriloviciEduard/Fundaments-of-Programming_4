from utils.ss import my_sort, my_filter
from utils.ut import asc, comp_x_desc, thr_pp,desc, comp_x_asc, comp_conc_asc, comp_conc_desc, eq, eq_name, ls_eq, ac_eq
from utils import bkt


class PlanesRepo():
    

    #constructor
    def __init__(self):
        
        self.__repo=[]
        
    def add_plane(self,obj):
        
        """
            input: A Plane.
            output: A modified repository.
            desc.: The method adds a new plane in the repository. 
        """
        
        self.__repo.append(obj)
        
        
    def add_passenger_in_plane(self,passenger,plane):
        
        """
            input: A Passenger and the name of a plane.
            output: A modified repository.
            desc.: The method adds a new passenger in the repository for a given plane. 
        """
        
        for el in self.__repo:
            if el.get_name()==plane:
                el.add_passenger(passenger)
                break
        
    def get_all_planes(self):
        
        """
            input: -
            output: A repository.
            desc.: The method returns all the values from the repository.
        """
        
        return self.__repo
    
    def clear_repo_pn(self):
        
        """
            input: -
            output: A modified repository.
            desc.: The method deletes all the values from the repository.
        """
        
        self.__repo=[]
        
    def del_plane(self,i):
        
        """
            input: An index.
            output: A modified repository.
            desc.: The method deletes the values from the repository for a given index.
        """
        
        if len(self.__repo)>i:  
            del(self.__repo[i])
        
    def up_plane(self,i,obj):
        
        """
            input: An index.
            output: A modified repository.
            desc.: The method updates the values from the repository for a given index.
        """
        
        if len(self.__repo)>i: 
            self.__repo[i]=obj
            
    def sort_plane_asc(self):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the passengers in the planes by the last name(asc.).
        """
        
        for el in self.__repo:
            lst=my_sort(el.get_list_passengers(),asc)
            el.set_list_passengers(lst)
            
            
    def sort_plane_desc(self):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the passengers in the planes by the last name(desc.).
        """
        
        for el in self.__repo:
            lst=my_sort(el.get_list_passengers(),desc)
            el.set_list_passengers(lst)
            
    def sort_plane_x_asc(self,x):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the planes according to the number of passengers with the first name starting with a given letter(asc.).
        """
        
    
        lst=my_sort(self.__repo,comp_x_asc,x)
        self.__repo=lst
            
            
    def sort_plane_x_desc(self,x):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the planes according to the number of passengers with the first name starting with a given letter(desc.).
        """
        
        lst=my_sort(self.__repo,comp_x_desc,x)
        self.__repo=lst
        
    def sort_plane_conc_asc(self):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the planes according to the string obtained by concat. nr.pass and nr.plane(asc.).
        """
        
        lst=my_sort(self.__repo,comp_conc_asc)
        self.__repo=lst
        
    def sort_plane_conc_desc(self):
        
        """
            input:-
            output: A modified repository.
            desc.: The method sorts the planes according to the string obtained by concat. nr.pass and nr.plane(desc.).
        """
        
        lst=my_sort(self.__repo,comp_conc_desc)
        self.__repo=lst
        
    def filter_33(self):
        
        """
            input:-
            output: A modified repository.
            desc.: The method identifies the planes with passengers with 3 letters of the passport equal.
        """
        
        lst=[]
        
        for el in self.__repo:
            
            l=my_filter(el.get_list_passengers(),thr_pp)
            
            if l!=[ ]:
                lst.append(el)
                
        
        return lst
    
    def pass_names(self,name,nr_pl):
        
        """
            input:-
            output: A modified repository.
            desc.: The method identifies the passengers from a given plane for which the first name or last name contain a given string.
        """
        
        
        for el in self.__repo:
            
            if el.get_name()==nr_pl:
                return my_filter(el.get_list_passengers(), eq, name)
            
    def sr_by_name(self,name):
        
        """
            input:-
            output: A modified repository.
            desc.: The method identifies the planes which have a passenger with a given name.
        """
        
        return my_filter(self.__repo, eq_name, name)
    
    def get_all_passengers_fromg_plane(self,name):
        
        """
            input:-
            output: A list of passengers.
            desc.: The method returns the list of passengers for a given plane.
        """
        
        for el in self.__repo:
            if el.get_name()==name:
                return el.get_list_passengers()
            
            
    def k_passengers(self,k):
        
        """
            input:-
            output: -
            desc.: The method forms groups of k passengers from the same plane but with different last names. 
        """
        
        for el in self.__repo:
            print(el.get_name(),":")
            bkt.Bkt(el.get_list_passengers(), k,ls_eq)
            
            print('\n\n')
            
    def k_planes(self,k):
        
        """
            input:-
            output: -
            desc.: The method forms groups of k planes with the same destination but belonging to different airline companies 
        """
        
        lst=[]
        lst.append(self.__repo[0])
        
        for i in range(1,len(self.__repo)):
            if self.__repo[0].get_destination()==self.__repo[i].get_destination():
                lst.append(self.__repo[i])
                
        bkt.Bkt(lst,k,ac_eq)
            
                
            
    def __len__(self):
        return len(self.__repo)
        
    def __str__(self):
        s=""
        
        for el in self.__repo:
            s+=str(el)+"\n"
            
        return s
        
        