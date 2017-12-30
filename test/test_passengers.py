import unittest
from domain.passengers import Passenger

class TestPassengers(unittest.TestCase):
    
    def test_create(self):
        ps=Passenger('Andrei','Gherasim',1295831098421)
        
        self.assertEqual(ps.get_first_name(),'Andrei')
        self.assertEqual(ps.get_last_name(),'Gherasim')
        self.assertEqual(ps.get_passport_number(),1295831098421)
        
    def test_set_fname(self):
        ps=Passenger()
        ps.set_first_name('Maccedonski')
        
        self.assertEqual(ps.get_first_name(),'Maccedonski')
        
    def test_set_lname(self):
        ps=Passenger()
        ps.set_last_name('Jean')
        
        self.assertEqual(ps.get_last_name(),'Jean')
        
    def test_set_ppnr(self):
        ps=Passenger()
        ps.set_passport_number(1295831098421)
        
        self.assertEqual(ps.get_passport_number(),1295831098421)
        

if __name__=='__main__':
    unittest.main()
        
