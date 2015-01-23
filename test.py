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
=======

import unittest
import hangman

class TestCase(unittest.TestCase):

    def test_correctAnswer(self):
        answer = hangman.checkCorrectAnswer("tac", "cat")
        self.assertTrue(answer)  #assertTrue

    def test_ncorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("ta", "cat")
        self.assertEqual(answer, False)

    def test_wrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

    def test_nwrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebra", "zebra")
        self.assertEqual(answer, False)
>>>>>>> 8a33bd6a4d6b5cbd1855ed2c8d0bd4b72de82ab2


if __name__ == "__main__":
    unittest.main()
