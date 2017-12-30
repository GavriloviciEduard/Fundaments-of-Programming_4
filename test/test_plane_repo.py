import unittest
from domain.planes import Plane
from infrastructure.planes_repo import PlanesRepo
from domain.passengers import Passenger

class PlanesRepoTest(unittest.TestCase):
    
    def test_add(self):
        r=PlanesRepo()
        p=Plane('Avion 1',2345,'WIZZ',200,'Honolulu',['Ion','Marcel',199724507890])
        r.add_plane(p)
        
        self.assertEqual(str(r),"Name:Avion 1 --- Number: 2345 --- Airline Company:WIZZ --- Number of seats:200 --- Destination:Honolulu --- List of passengers:['Ion', 'Marcel', 199724507890]\n")
        
    def test_get_all_planes(self):
        r=PlanesRepo()
        p1=Plane('Avion 1',2345,'WIZZ',200,'Honolulu',['Ion','Marcel',199724507890])
        p2=Plane('Avion 2',2346,'WIZZ',200,'Argentina',['Marius','Marcel',199724507891])  
        r.add_plane(p1)
        r.add_plane(p2)
        
        self.assertEqual(str(r),"Name:Avion 1 --- Number: 2345 --- Airline Company:WIZZ --- Number of seats:200 --- Destination:Honolulu --- List of passengers:['Ion', 'Marcel', 199724507890]\nName:Avion 2 --- Number: 2346 --- Airline Company:WIZZ --- Number of seats:200 --- Destination:Argentina --- List of passengers:['Marius', 'Marcel', 199724507891]\n")  
     
    def test_add_passenger_in_plane(self):
        r=PlanesRepo()
        p=Plane('Avion 1',2345,'WIZZ',200,'Honolulu',['Ion','Marcel',199724507890])
        r.add_plane(p)
        passenger=Passenger('Ionut','Cercel',199724507891)
        r.add_passenger_in_plane(passenger, 'Avion 1')
        
        self.assertEqual(str(r),"Name:Avion 1 --- Number: 2345 --- Airline Company:WIZZ --- Number of seats:200 --- Destination:Honolulu --- List of passengers:['Ion', 'Marcel', 199724507890, First name:Ionut --- Last name:Cercel --- Passport number:199724507891]\n")
    
    def test_get_all_passengers_fromg_plane(self):
        r=PlanesRepo()
        p=Plane('Avion 1',2345,'WIZZ',200,'Honolulu',['Ion','Marcel',199724507890])
        r.add_plane(p)
        
        lst=r.get_all_passengers_fromg_plane('Avion 1')
        
        self.assertEqual(str(lst),"['Ion', 'Marcel', 199724507890]")
               
if __name__=='__main__':
    unittest.main()
    
    