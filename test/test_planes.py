import unittest
from domain.planes import Plane

class TestPlanes(unittest.TestCase):
    
    def test_create(self):
        
        p=Plane('Avion 1',2345,'WIZZ',200,'Honolulu',['Ion','Marcel',199724507890])
        
        self.assertEqual(p.get_name(),'Avion 1')
        self.assertEqual(p.get_number(),2345)
        self.assertEqual(p.get_airline_company(),'WIZZ')
        self.assertEqual(p.get_number_seats(),200)
        self.assertEqual(p.get_destination(),'Honolulu')
        self.assertEqual(p.get_list_passengers(),['Ion','Marcel',199724507890])
        
    def test_set_name(self):
        p=Plane()
        p.set_name('Avion 2')
        
        self.assertEqual(p.get_name(),'Avion 2')
        
    def test_set_number(self):
        p=Plane()
        p.set_number(12345)
        
        self.assertEqual(p.get_number(),12345)
        
    def test_set_airline_company(self):
        p=Plane()
        p.set_airline_company("WIZZ")
        
        self.assertEqual(p.get_airline_company(),'WIZZ')
        
    def test_set_number_seart(self):
        p=Plane()
        p.set_number_seats(456)
        
        self.assertEqual(p.get_number_seats(),456)
        
    def test_set_destination(self):
        p=Plane()
        p.set_destination('Pocreaca')
        
        self.assertEqual(p.get_destination(),'Pocreaca')
        
    def test_set_list_passengers(self):
        p=Plane()
        p.set_list_passengers(['Ion','Marcel',199724507890])
        
        self.assertEqual(p.get_list_passengers(),['Ion','Marcel',199724507890])
        
        

if __name__=='__main__':
    unittest.main()
    
        
        
        