import unittest
from operacoes import soma, subtracao


class TestOperacoes(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 4), 6)


if __name__ == '__main__':
    unittest.main()
