import pytest

# Para instalar o Pytest, você pode usar o seguinte 
# comando no terminal: pip install pytest

from operacoes import soma, subtracao


def test_soma_positivos():
    assert soma(2, 3) == 5



def test_soma_negativos():
    assert soma(-1, -1) == -2


def test_subtracao():
    assert subtracao(10, 4) == 6


@pytest.mark.parametrize(
    "a,b,esperado",
    [(2, 3, 5), (-1, -1, -2), (0, 0, 0)]
)
def test_soma_parametrizado(a, b, esperado):
    assert soma(a, b) == esperado
