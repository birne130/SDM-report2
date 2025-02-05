#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (-1, calc(3,1200))

        def test_sample2 (self):
                self.assertEqual (-1, calc(-50,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc(-100,1000))

        def test_sample4 (self):
                self.assertEqual (-1, calc(5.6,600))

        def test_sample5 (self):
                self.assertEqual (-1, calc(64,1422.1))

        def test_sample6 (self):
                self.assertEqual (-1, calc(84.5,92.8))
        
        def test_sample7 (self):
                self.assertEqual (-1, calc('a',300))

        def test_sample8 (self):
                self.assertEqual (-1, calc(325,'b'))

        def test_sample9 (self):
                self.assertEqual (-1, calc('s','g'))

        def test_sample10 (self):
                self.assertEqual (-1, calc(1000,245))

        def test_sample11 (self):
                self.assertEqual (-1, calc(500,1000))

        def test_sample12 (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_sample13 (self):
                self.assertEqual (-1, calc(0,45))

        def test_sample14 (self):
                self.assertEqual (-1, calc(50,0))

        def test_sample15 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample16 (self):
                self.assertEqual (-1, calc((1.0 - 0.01),245))

        def test_sample17 (self):
                self.assertEqual (-1, calc(325,(1.0 - 0.01)))

        def test_sample18 (self):
                self.assertEqual (-1, calc((1.0 - 0.01),(1.0 - 0.01)))

        def test_sample19 (self):
                self.assertEqual (-1, calc(24,(999.0 + 0.01)))

        def test_sample20 (self):
                self.assertEqual (-1, calc((999.0 + 0.01),83))

        def test_sample21 (self):
                self.assertEqual (-1, calc((999.0 + 0.01),(999.0 + 0.01)))
        
        def test_sample22 (self):
                self.assertEqual (63, calc(7, 9))

        def test_sample23 (self):
                self.assertEqual (500, calc(25, 20))
        
        def test_sample24 (self):
                self.assertEqual (40000, calc(200, 200))