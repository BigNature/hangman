__author__ = 'user'

import unittest
import hangman

class check(unittest.TestCase):

    def test_true(self):
        ret = hangman.checkCorrectAnswer('tac','cat')
        self.assertTrue(ret)

    def test_false(self):
        ret = hangman.checkCorrectAnswer('ta','cat')
        self.assertEqual(ret,False)


if __name__ == "__main__":
    unittest.main()