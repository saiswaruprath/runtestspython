import unittest
import sys
sys.path.append('/home//project//xzceb-flask_eng_fr//final_project//machinetranslation')
from translator import english_to_french, french_to_english

class testForEngToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(None), None)


class testForFrenchToEng(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(None), None)



unittest.main()
