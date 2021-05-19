# Using setUp method
# The tests don't run in order necessarily
# from unittest import TestCase

import unittest
import demo


class TestDemo(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    def setUp(self):   # initializing the needed values for the tests  FIXTURE
        # print('setUp')
        self.p1 = demo.Person('Leonardo', 'Miranda')
        self.c1 = demo.Operations(5, -5)

    # sum
    def test_get_sum(self):
        pass

    # sub
    def test_get_sub(self):
        pass

    # mult
    def test_get_mult(self):
        pass

    # div
    def test_get_div(self):
        pass

    # double
    def test_get_double(self):
        pass

    # square
    def test_get_square(self):
        pass

    # area_quadrado
    def test_area_quadrado(self):
        pass

    # area_retangulo
    def test_area_retangulo(self):
        pass

    def test_get_fullname(self):
        self.assertEqual(self.p1.get_fullname(), 'Leonardo Miranda')

    def test_get_email(self):
        self.assertEqual(self.p1.get_email(), 'leonardo.miranda@email.com.br')

    def tearDown(self):  # deleting the needed values for the tests
        # print('tearDown')
        del self.p1
        del self.c1


if __name__ == '__main__':
    unittest.main()


# python -m unittest file_name.py