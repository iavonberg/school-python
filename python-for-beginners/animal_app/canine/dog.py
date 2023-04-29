from animal_app.animal import Animal
import unittest

class Dog(Animal):
    def __init__(self):
        self.legs = 4
        self.wings = False
        self.sounds = 'Barks'
        
    def is_thirsty(self):
        return 'pants'
    
class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()

    def test_isThirsty(self):
        self.dog.is_thirsty()
        self.assertEqual(self.dog.is_thirsty(), 'pants')

if __name__ == '__main__':
    unittest.main()