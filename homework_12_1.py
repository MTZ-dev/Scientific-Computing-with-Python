#EXERCISE 12.1

import unittest
import math
from homework_6 import Vector

class TestVector(unittest.TestCase):

    def setUp(self):

        self.unit_vector = Vector(1.,1.,1.)
        self.zero_vector = Vector(0.,0.,0.)
        self.vector1 = Vector(1., 2., 3.)
        self.vector2 = Vector(2., -3., 2.)

   
    def test_mul(self):
        
        self.assertEqual(self.zero_vector * self.vector1, 0.)
        self.assertEqual(self.vector1 * self.vector2, 2)
        self.assertEqual(self.vector1 * self.unit_vector, self.vector1.x + self.vector1.y + self.vector1.z)
        self.assertNotEqual(self.vector1 * self.unit_vector, 0)
        self.assertTrue(self.vector2 * self.vector2 > 0)


    def test_cross(self):
        
        self.assertEqual(self.vector1.cross(self.zero_vector), self.zero_vector)
        self.assertEqual(self.vector1.cross(self.vector2), Vector(13.0, 4.0, -7.0))
        self.assertEqual(self.vector1.cross(self.unit_vector), Vector(-1.,2.,-1.))


    def test_lenght(self):
        
        self.assertAlmostEqual(self.vector1.length(), math.sqrt(self.vector1 * self.vector1))
        self.assertTrue(self.vector2.length() > 0)
        self.assertTrue((self.vector1 + self.vector2).length() <= (self.vector1.length() + self.vector2.length())) # Triangle Inequality


    def test_Vector_exceptions(self):   
        
        with self.assertRaises(ValueError):   
            Vector(1,1,1) # my class only accepts floats for initialization


    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()


