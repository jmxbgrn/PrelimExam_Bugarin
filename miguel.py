import unittest

def check(MIGUEL):

    return MIGUEL>=MIGUEL

class myTest(unittest.TestCase):

    def test(self):

        self.assertTrue(check(1))

if __name__ == '__main__':

    unittest.main()