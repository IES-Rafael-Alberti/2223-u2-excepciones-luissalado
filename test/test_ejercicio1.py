from src.ejercicio1 import leernumero, proceso, mensaje


def test_leernumero(monkeypatch):
    # test caso 1:
    input_values = 1
    def mock_input(s):
        return input_values
    monkeypatch.setattr('builtins.input', mock_input)
    assert leernumero() == 1
    
def test_proceso():
    assert proceso(5) == ["Tienes 1 años", "Tienes 2 años", "Tienes 3 años", "Tienes 4 años", "Tienes 5 años"]
    