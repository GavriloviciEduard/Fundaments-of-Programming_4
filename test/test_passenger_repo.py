import unittest
from domain.passengers import Passenger
from infrastructure.passengers_repo import PassengersRepo

class PassengersRepoTest(unittest.TestCase):
    
    
    def test_add_passenger(self):
        r=PassengersRepo()
        p=Passenger("Ion","Marcel",199724507890)
        r.add_passenger(p)
        
        self.assertEqual(str(r),"First name:Ion --- Last name:Marcel --- Passport number:199724507890\n")
        
        
    def test_get_all_passengers(self):
        r=PassengersRepo()
        p1=Passenger("Ion","Marcel",199724507890)
        p2=Passenger("Andrei","Marcel",199724507891)
        p3=Passenger("Ionunt","Marius",199724507892)
        r.add_passenger(p1)
        r.add_passenger(p2)
        r.add_passenger(p3)
        
        
        lst=r.get_all_passengers()
        
        self.assertEqual(str(lst),"[First name:Ion --- Last name:Marcel --- Passport number:199724507890, First name:Andrei --- Last name:Marcel --- Passport number:199724507891, First name:Ionunt --- Last name:Marius --- Passport number:199724507892]")
        
        

if __name__=='__main__':
    unittest.main()
        
        