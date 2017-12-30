import os
from utils.ss import search
from utils.ut import pl_eq,eq_nrpass




class PPUI():
    
    def __init__(self,cntr):
        
        self.__controller=cntr
        
        
    
    
    @staticmethod
    def menu():
        
        os.system("cls")
        print("--------------------PLANES AND PASSENGERS--------------------")
        print("1.Print all planes.")
        print("2.Print all lists of passengers.")
        print("3.Create a new plane.")
        print("4.Delete all planes.")
        print("5.Delete all the lists of passengers.")
        print("6.Delete a plane (by index).")
        print("7.Delete a list of passengers from a given plane (by index).")
        print("8.Update/Replace a plane (by index).")
        print("9.Update/Replace a list of passengers from a given plane (by index).")
        print("10.Sort the passengers in the planes by the last name(asc.).")
        print("11.Sort the passengers in the planes by the last name(desc.).")
        print("12.Sort planes according to the number of passengers with the first name starting with a given letter(asc.).")
        print("13.Sort planes according to the number of passengers with the first name starting with a given letter(desc.).")
        print("14.Sort planes according to the string obtained by concat. nr.pass and nr.plane(asc.).")
        print("15.Sort planes according to the string obtained by concat. nr.pass and nr.plane(desc.).")
        print("16.Identify the planes with passengers with 3 letters of the passport equal.")
        print("17.Identify the passengers from a given plane for which the first name or last name contain a given string.")
        print("18.Identify planes which have a passenger with a given name.")
        print("19.Add a passenger in a given plane.")
        print("20.Form groups of k passengers from the same plane but with different last names.")
        print("21.Form groups of k planes with the same destination but belonging to different airline companies")
        
        print("0.Exit.")
        
    @staticmethod
    def read_number():
        
        while True:
            
            try:
                nr=int(input("Enter a number(decimal): "))
                
                if nr>0:
                    break
            except:
                print("The value you entered is wrong! Try again!")
                
            print("The number must be >0 !")
                
        return nr
    
    
    @staticmethod
    def read_index():
        
        while True:
            
            try:
                nr=int(input("Enter a number(decimal): "))
                if(nr>-1):
                    break
            except:
                print("The value you entered is wrong! Try again!")
                
            print("The number must be >0 !")
                
        return nr
    
    
    @staticmethod   
    def read_string():
        
        
        while True:
            
            try:
                st=input("Enter a string(non-empty): ")
                
                if len(st):
                    break
            except:
                print("Something went wrong! Try again! ")
                
            print("The string must not be empty! Try again!")
                
        
        return st.strip()
    
    @staticmethod
    def read_letter():
        
        l=''
        
        while True:
            
            try:
                l=input("Enter a character(single):")
                
                if(len(l)==1):
                    break
            except:
                print("Something went wrong!!")
                
            print("Enter only a single character!")
            
        
        return l
    
    
    
    
    def read_first_data(self):
        
        print("Enter the number of planes you want to be read:")
        nr_planes=PPUI.read_number()
        lst_pass=[]
        
        
        
        while nr_planes:
            
            print("Enter the name of the plane:")
            name_plane=PPUI.read_string()
            print("Enter the number of the plane:")
            number_plane=PPUI.read_number()
            print("Enter the name of the airline company:")
            air_comp=PPUI.read_string()
            print("Enter the number of seats:")
            nr_sts=PPUI.read_number()
            print("Enter the name of the destination:")
            dest=PPUI.read_string()
            
            print("Enter the number of passengers:")
            nr_pass=0
            
            while nr_pass>nr_sts or not(nr_pass):
                nr_pass=PPUI.read_number()
                if nr_pass>nr_sts:
                    print("The number of passengers must be <= to the number of seats!")
            
            while nr_pass:
                
                lst=[]
                    
                print("Enter the first name of a passenger:")
                fs_name=PPUI.read_string()
                print("Enter the last name of a passenger:")
                ls_name=PPUI.read_string()
                
                ps_nr=0
                
                while ps_nr<1000:
                            print("Enter the passport number of a passenger:")
                            ps_nr=PPUI.read_number()
                            
                            if ps_nr<1000:
                                print("The len. of the passport number must be >4!")
                
                lst.append(fs_name)
                lst.append(ls_name)
                lst.append(ps_nr)
                
                lst_pass.append(lst)
                nr_pass-=1
                
            self.__controller.add_cr_pln(name_plane,number_plane,air_comp,nr_sts,dest,lst_pass)
            nr_planes-=1
                
                
                
                
                    
    def start(self):
        
        
        
        
        self.read_first_data()
        
        
        
            
        while True:
            
            PPUI.menu()
            
            try:
                opt=input("Select an option:")
            except:
                input("Something went wrong! Press any key...")
                
            
            if opt=='1':
                lst=self.__controller.get_all_pln()
                index=0
                
                for el in lst:
                    
                    print('\n\n',index,"=>",str(el))
                    print('\n\n')
                   
                    index+=1
                    
                input("Press any key...")
                
            elif opt=='2':
                lst=self.__controller.get_all_pas()
                index=0
                
                for el in lst:
                    print('\n\n',index,"=>",str(el))
                    index+=1
                    
                input("Press any key...")
                
            elif opt=='3':
                
                lst_pass=[]
                print("Enter the name of the plane:")
                name_plane=PPUI.read_string()
                print("Enter the number of the plane:")
                number_plane=PPUI.read_number()
                print("Enter the name of the airline company:")
                air_comp=PPUI.read_string()
                print("Enter the number of seats:")
                nr_sts=PPUI.read_number()
                print("Enter the name of the destination:")
                dest=PPUI.read_string()
            
                print("Enter the number of passengers:")
                nr_pass=0
            
                while nr_pass>nr_sts or not(nr_pass):
                    nr_pass=PPUI.read_number()
                    if nr_pass>nr_sts:
                        print("The number of passengers must be <= to the number of seats!")
            
                while nr_pass:
                
                    lst=[]
                    
                    print("Enter the first name of a passenger:")
                    fs_name=PPUI.read_string()
                    print("Enter the last name of a passenger:")
                    ls_name=PPUI.read_string()
                    
                    ps_nr=0
                
                    while ps_nr<1000:
                        print("Enter the passport number of a passenger:")
                        ps_nr=PPUI.read_number()
                            
                        if ps_nr<1000:
                            print("The len. of the passport number must be >4!")
                
                    lst.append(fs_name)
                    lst.append(ls_name)
                    lst.append(ps_nr)
                
                    lst_pass.append(lst)
                    nr_pass-=1
                
                self.__controller.add_cr_pln(name_plane,number_plane,air_comp,nr_sts,dest,lst_pass)
                
            elif opt=='4':
                self.__controller.clear_pln()
                input("All planes have been deleted! Press any key...")
                
            elif opt=='5':
                self.__controller.clear_pas()
                input("All passengers have been deleted! Press any key...")
                
            elif opt=='6':
                print("Enter an index:")
                i=PPUI.read_index()
                self.__controller.del_pln(i)
                
            elif opt=='7':
                print("Enter an index:")
                i=PPUI.read_index()
                self.__controller.del_pas(i)
                
            elif opt=='8':
                
                
                
                print("Enter an index:")
                i=PPUI.read_index()
                
                if self.__controller.len_pln()>i:
                
                    lst_pass=[]
                    print("Enter the name of the plane:")
                    name_plane=PPUI.read_string()
                    print("Enter the number of the plane:")
                    number_plane=PPUI.read_number()
                    print("Enter the name of the airline company:")
                    air_comp=PPUI.read_string()
                    print("Enter the number of seats:")
                    nr_sts=PPUI.read_number()
                    print("Enter the name of the destination:")
                    dest=PPUI.read_string()
            
                    print("Enter the number of passengers:")
                    nr_pass=0
            
                    while nr_pass>nr_sts or not(nr_pass):
                        nr_pass=PPUI.read_number()
                        if nr_pass>nr_sts:
                            print("The number of passengers must be <= to the number of seats!")
            
                    while nr_pass:
                
                        lst=[]
                    
                        print("Enter the first name of a passenger:")
                        fs_name=PPUI.read_string()
                        print("Enter the last name of a passenger:")
                        ls_name=PPUI.read_string()
                        
                        ps_nr=0
                        
                        while ps_nr<1000:
                            print("Enter the passport number of a passenger:")
                            ps_nr=PPUI.read_number()
                            
                            if ps_nr<1000:
                                print("The len. of the passport number must be >4!")
                
                        lst.append(fs_name)
                        lst.append(ls_name)
                        lst.append(ps_nr)
                
                        lst_pass.append(lst)
                        nr_pass-=1
                    
                        self.__controller.up_pln(name_plane,number_plane,air_comp,nr_sts,dest,lst_pass,i)
                
            elif opt=='9':
                
                print("Enter an index:")
                i=PPUI.read_index()
                
                if self.__controller.len_pass()>i:
                
                    print("Enter the first name of a passenger:")
                    fs_name=PPUI.read_string()
                    print("Enter the last name of a passenger:")
                    ls_name=PPUI.read_string()
                    
                    ps_nr=0
                
                    while ps_nr<1000:
                        print("Enter the passport number of a passenger:")
                        ps_nr=PPUI.read_number()
                            
                        if ps_nr<1000:
                            print("The len. of the passport number must be >4!")
                
                    self.__controller.up_pas(fs_name,ls_name,ps_nr,i)
                    
                    
            elif opt=='10':
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_asc()
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
            elif opt=='11':
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_desc()
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
            elif opt=='12':
                
                
                x=PPUI.read_letter()
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_x_asc(x)
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
                    
            elif opt=='13':
                
               
                x=PPUI.read_letter()
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_x_desc(x)
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
                    
            elif opt=='14':
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_conc_asc()
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
            elif opt=='15':
                
                if self.__controller.len_pass():
                    self.__controller.sort_pl_conc_desc()
                    
                else:
                    input("Nothing to sort! Press any key...")
                    
            elif opt=='16':
                
                
                
                lst=self.__controller.filter_3()
                
                index=0
                
                for el in lst:
                    
                    print('\n\n',index,"=>",str(el))
                    print('\n\n')
                   
                    index+=1
                    
                input("Press any key...")
                
            elif opt=='17':
                
                print("Enter a plane:")
                nr_pl=PPUI.read_string()
                
                plane=self.__controller.get_all_pln()
                
                if not(search(plane,nr_pl,pl_eq)):
                    print("Enter a name:")
                    name=PPUI.read_string()
                    s=self.__controller.pass_nms(name,nr_pl)
                    
                    for el in s:
                        print(str(el))
                    
                else:
                    print("Nothing to search!!")
                    
                input("Press any key...")
                
                
            elif opt=='18':
                
                print("Enter first name:")
                f=PPUI.read_string()
                
                print("Enter last name:")
                l=PPUI.read_string()
                
                n=f + " " + l
                
                s=self.__controller.sr_by_nm(n)
                
                for el in s:
                    print(str(el))
                    
                input("Press any key...")
                
            elif opt=='19':
                
                print("Enter a plane:")
                n_plane=PPUI.read_string()
                
                plane=self.__controller.get_all_pln()
                
                if not(search(plane,n_plane,pl_eq)):
                    
                    print("Enter the first name of a passenger:")
                    fs_name=PPUI.read_string()
                    print("Enter the last name of a passenger:")
                    ls_name=PPUI.read_string()
                    
                    ps_nr=0
                    
                    while ps_nr<1000:
                            print("Enter the passport number of a passenger:")
                            ps_nr=PPUI.read_number()
                            
                            if ps_nr<1000:
                                print("The len. of the passport number must be >4!")
                    
                    ps=self.__controller.get_all_pas_gpl(n_plane)
                    
                    if search(ps,ps_nr,eq_nrpass):
                        self.__controller.add_p_in_p(fs_name,ls_name,ps_nr,n_plane)
                        
                    else:
                        print("The passenger already exists!")
                        
                else:
                    print("The plane doesn't exist!")
                    
                input("Press any key...")
                
            elif opt=='20':
        
                k=PPUI.read_number()      
                self.__controller.k_pass(k)
                input("Press any key...")
                
            elif opt=='21':
                k=PPUI.read_number()
                self.__controller.k_plns(k)
                input("Press any key...")
                             
                
            elif opt=='0':
                break
            
            else:
                input("The option doesn't exist! Try again! Press any key...")
         
        
        
