import unittest
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    """
    Sad path
    """
    
    #type of input -- string; correct output -- Empty list
    
    def test_str_01(self):
        self.assertEqual([ ], mc.makeChange('alpha'))
    
    def test_str_02(self):
        self.assertEqual([ ], mc.makeChange('$123'))
        
    def test_str_03(self):
        self.assertEqual([ ], mc.makeChange('123'))
        
    def test_str_04(self):
        self.assertEqual([ ], mc.makeChange('.3435'))
    
    def test_str_05(self):
        self.assertEqual([ ], mc.makeChange(''))
        
    def test_str_06(self):
        self.assertEqual([ ], mc.makeChange('-5.4'))
    
    #type of input -- negative number; correct output -- Empty list
    
    def test_neg_num_01(self):
        self.assertEqual([ ], mc.makeChange(-9))
    
    def test_neg_num_02(self):
        self.assertEqual([ ], mc.makeChange(-2.33))
        
    def test_neg_num_03(self):
        self.assertEqual([ ], mc.makeChange(-23434))
        
    def test_neg_num_04(self):
        self.assertEqual([ ], mc.makeChange(-9))
        
    def test_neg_num_05(self):
        self.assertEqual([ ], mc.makeChange(-10e5))
        
    def test_neg_num_06(self):
        self.assertEqual([ ], mc.makeChange(-0.5))
        
    def test_neg_num_07(self):
        self.assertEqual([ ], mc.makeChange(-0.43))
                          
    #type of input -- None; correct output -- Empty list
    def test_empty_input(self):
        self.assertEqual([ ], mc.makeChange())
        
    #type of input -- positive number great than or equal to 100; correct output -- Empty list
    
    def test_outofrange_input_01(self):
        self.assertEqual([ ], mc.makeChange(100))
        
    def test_outofrange_input_02(self):
        self.assertEqual([ ], mc.makeChange(1100))
    
    
    
    """
    Happy path
    """
     
    #type of input -- legal input(non-negative integer or floats)
    def test_n_neg_01(self):
        self.assertEqual([0,0,0,3,0,0,0,0], mc.makeChange(3))
    
    def test_n_neg_02(self):
        self.assertEqual([0,0,0,0,0,0,0,0], mc.makeChange(0))
        
    def test_n_neg_03(self):
        self.assertEqual([0,0,0,3,1,0,0,1], mc.makeChange(3.26))
    
    def test_n_neg_04(self):
        self.assertEqual([0,0,0,3,1,0,0,1], mc.makeChange(3.2634355))
    
    def test_n_neg_05(self):
        self.assertEqual([0,0,1,0,0,0,0,0], mc.makeChange(5))
        
    def test_n_neg_06(self):
        self.assertEqual([1,1,1,1,1,1,1,1], mc.makeChange(36.41))
    
    def test_n_neg_07(self):
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1.001))
    
    def test_n_neg_08(self):
        self.assertEqual([0,0,0,1,0,0,0,1], mc.makeChange(1.005))
         
    def test_n_neg_09(self):
        self.assertEqual([0,0,0,1,0,0,0,0], mc.makeChange(1.004))
        
    def test_n_neg_10(self):
        self.assertEqual([0,0,0,0,2,1,1,2], mc.makeChange(.67))
        
    def test_n_neg_11(self):
        self.assertEqual([0,0,0,1,0,0,0,1], mc.makeChange(amount=1.005))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
