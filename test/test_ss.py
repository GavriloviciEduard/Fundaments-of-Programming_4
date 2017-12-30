import unittest
from utils.ss import my_filter, my_sort

def up(a,b):
        return a>b
    
class TESTSS(unittest.TestCase):
    
    
    def test_my_sort(self):
        lst=[2,3,5,78,3,6,7,9,1,35,5,66767,32,423,4324,6565,123,5345,23]
        lst=my_sort(lst,up)
        
        self.assertEqual(lst,[1, 2, 3, 3, 5, 5, 6, 7, 9, 23, 32, 35, 78, 123, 423, 4324, 5345, 6565, 66767])
        
    def test_my_filter(self):
        lst=[0,0,0,0,0,-2,-5,21,323,34,53,12,423,312,321,-22,-2,0,9.8,-0.1]
        lst=my_filter(lst, up ,0)
        
        self.assertEqual(lst,[21, 323, 34, 53, 12, 423, 312, 321, 9.8])
        

if __name__=="__main__":
    unittest.main()
    
    
    
    
        
    