from domain.passengers import Passenger
from domain.planes import Plane
from utils.ss import search
from utils.ut import equal_pass
from utils.ut import equal_plane

class AppController():

    def __init__(self, pln_repo, pas_repo):
        
        """
            input: Two repositories.
            output: A controller.
            desc.: Constructor. 
        """
        
        self.__plane_repo=pln_repo
        self.__passenger_repo=pas_repo
        
        
    def get_all_pln(self):
        
        """
            input: A controller.
            output: A repository(Plane).
            desc.: The controller returns all the values of the repository. 
        """
        
        return self.__plane_repo.get_all_planes()
        
    def get_all_pas(self):
        
        """
            input: A controller.
            output: A repository(Passenger).
            desc.: The controller returns all the values of the repository. 
        """
        
        return self.__passenger_repo.get_all_passengers()
    
    
    def get_all_pas_gpl(self,name_plane):
        
        """
            input: A controller.
            output: A list of passengers.
            desc.: The controller returns all the passengers from a given plane. 
        """
        
        return self.__plane_repo.get_all_passengers_fromg_plane(name_plane)
    
        
    def add_cr_pln(self,n,nr,arc,nrs,dest,lps):
        
        """
            input: Data for the the Plane and Passenger
            output: -
            desc.: The controller creates a Plane. 
        """
        
        lst_ps=[]
    
        
        for el in lps:
            passenger=Passenger(el[0],el[1],el[2])
            if search(self.__passenger_repo.get_all_passengers(),passenger.get_passport_number(),equal_pass) and search(self.__plane_repo.get_all_planes(),nr,equal_plane) :
                lst_ps.append(passenger)
                self.__passenger_repo.add_passenger(passenger)
                
                
            
        plane=Plane(n,nr,arc,nrs,dest,lst_ps)
        if search(self.__plane_repo.get_all_planes(), plane.get_number(),equal_plane):
            self.__plane_repo.add_plane(plane)
            
    def add_p_in_p(self,fs_name,ls_name,ps_nr,n_plane):
        
        """
            input: Data for a Passenger and the name of a plane.
            output: -
            desc.: The controller adds a passenger in a given plane.
        """
        
        passenger=Passenger(fs_name,ls_name,ps_nr)
        self.__passenger_repo.add_passenger(passenger)
        self.__plane_repo.add_passenger_in_plane(passenger,n_plane)
        
              
    def clear_pln(self):
        
        """
            input: A controller.
            output: -
            desc.: The controller deletes all the data from the repository(Plane). 
        """
        self.__plane_repo.clear_repo_pn()
        
    def clear_pas(self):
        
        """
            input: A controller.
            output: -
            desc.: The controller deletes all the data from the repository(Passenger). 
        """
        self.__passenger_repo.clear_repo_ps()
        
    def del_pln(self,i):
        
        """
            input: A controller and an index.
            output: -
            desc.: The controller deletes a plane from a given index. 
        """
        
        self.__plane_repo.del_plane(i)
        
    def del_pas(self,i):
        
        """
            input: A controller and an index.
            output: -
            desc.: The controller deletes a passenger from a given index. 
        """
        self.__passenger_repo.del_passenger(i)
        
    def up_pln(self,n,nr,arc,nrs,dest,lps,indx):
        
        """
            input: Data for a Plan and an index.
            output: -
            desc.: The controller updates a Plane from a given index. 
        """
        
        plane=Plane(n,nr,arc,nrs,dest,lps)
        
        self.__plane_repo.up_plane(indx,plane)
        
    def up_pas(self,fn,ln,nrp,indx):
        
        """
            input: Data for a Plan and an index.
            output: -
            desc.: The controller updates a Passenger from a given index. 
        """
        
        passenger=Passenger(fn,ln,nrp)
        
        self.__passenger_repo.up_passenger(indx,passenger)
        
    def len_pln(self):
        
        """
            input: -
            output: -
            desc.: The controller returns the lenght of the repository(Plane). 
        """
        
        return len(self.__plane_repo)
    
    def len_pass(self):
        
        """
            input: -
            output: -
            desc.: The controller returns the lenght of the repository(Passenger). 
        """
        
        return len(self.__passenger_repo)
    
    def sort_pl_asc(self):
        
        """
            input:-
            output:-
            desc.: The controller sorts the passengers in the planes by the last name(asc.).
        """
        
        self.__plane_repo.sort_plane_asc()
        
    def sort_pl_desc(self):
        
        """
            input:-
            output:-
            desc.: The controller sorts the passengers in the planes by the last name(desc.).
        """
        
        self.__plane_repo.sort_plane_desc()
        
    def sort_pl_x_asc(self,x):
        
        """
            input:-
            output:-
            desc.: The controller sorts the planes according to the number of passengers with the first name starting with a given letter(asc.).
        """
        
        self.__plane_repo.sort_plane_x_asc(x)
        
    def sort_pl_x_desc(self,x):
        
        """
            input:-
            output:-
            desc.: The controller sorts the planes according to the number of passengers with the first name starting with a given letter(desc.).
        """
        
        self.__plane_repo.sort_plane_x_desc(x)
        
    def sort_pl_conc_asc(self):
        
        """
            input:-
            output:-
            desc.: The controller sorts the planes according to the string obtained by concat. nr.pass and nr.plane(asc.).
        """
        
        self.__plane_repo.sort_plane_conc_asc()
        
    def sort_pl_conc_desc(self):
        
        """
            input:-
            output:-
            desc.: The controller sorts the planes according to the string obtained by concat. nr.pass and nr.plane(desc.).
        """
        
        self.__plane_repo.sort_plane_conc_desc()
        
        
    def filter_3(self):
        
        """
            input:-
            output:-
            desc.: The controller identifies the planes with passengers with 3 letters of the passport equal.
        """
        
        return self.__plane_repo.filter_33()
    
    def pass_nms(self,name,nr_pl):
        
        """
            input: A name and the name of a plane.
            output:-
            desc.: The controller identifies the passengers from a given plane for which the first name or last name contain a given string.
        """
        
        return self.__plane_repo.pass_names(name,nr_pl)
    
    def sr_by_nm(self,n):
        
        """
            input:-
            output:-
            desc.: The controller identifies the planes which have a passenger with a given name.
        """
        
        return self.__plane_repo.sr_by_name(n)
    
    
    def k_pass(self,k):
        
        """
            input:-
            output:-
            desc.: The controller forms groups of k passengers from the same plane but with different last names.
        """
        
        self.__plane_repo.k_passengers(k)
        
    def k_plns(self,k):
        
        """
            input:-
            output:-
            desc.: The controller forms  groups of k planes with the same destination but belonging to different airline companies. 
        """
        
        self.__plane_repo.k_planes(k)  
    
        
        
    def __str__(self):
        return str(self.__plane_repo)+" " + str(self.__passenger_repo)
    
    def __repr__(self):
        return str(self)
        
        
    
        
        
        