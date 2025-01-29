from io import StringIO

def test_char_counter(monkeypatch, capsys):
    from char_counter import char_counter

    monkeypatch.setattr(
        'sys.stdin', 
        StringIO("Well hello there!@\n")
    )
    char_counter()
    captured = capsys.readouterr()
    assert "'W': 1" in captured.out
    assert "'e': 4" in captured.out
    assert "'l': 4" in captured.out
    assert "' ': 2" in captured.out
    assert "'h': 2" in captured.out
    assert "'o': 1" in captured.out
    assert "'t': 1" in captured.out
    assert "'r': 1" in captured.out
    assert "'!': 1" in captured.out
    assert "'@': 1" in captured.out

    monkeypatch.setattr('sys.stdin', StringIO("\n"))
    char_counter()
    captured = capsys.readouterr()
    assert "{}" in captured.out

def test_duplicate_remover(capsys):
    from duplicate_remover import duplicate_remover
    duplicate_remover()
    captured = capsys.readouterr()
    assert "[1, 4, 3, 2, 5, 7, 9]" in captured.out

def test_even_square_sum(monkeypatch, capsys):
    from even_square_sum import even_square_sum

    even_square_sum()
    captured = capsys.readouterr()
    assert "44984" in captured.out

def test_grocery_calculator(monkeypatch, capsys):
    from grocery_calculator import grocery_calculator
    inputs = iter(['bread', 'milk', 'eggs', 'butter', 'eggs', ''])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    grocery_calculator()
    captured = capsys.readouterr()
    assert '$21' in captured.out

    monkeypatch.setattr('builtins.input', lambda msg: '')
    grocery_calculator()
    captured = capsys.readouterr()
    assert '$0' in captured.out

def test_temperature_calculator(monkeypatch, capsys):
    from temperature_calculator import temperature_calculator

    inputs = iter(['40', '28', '64', 'quit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    temperature_calculator()
    captured = capsys.readouterr()
    assert '40.0' in captured.out
