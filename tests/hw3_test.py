import pytest

def test_multilingual_greeter():
    from multilingual_greeter import get_multilingual_greeting

    assert get_multilingual_greeting("Bob") == "Hola Bob"
    assert get_multilingual_greeting("Bob", language='spanish') == "Hola Bob"
    assert get_multilingual_greeting("Bob", language='english') == "Hello Bob"
    assert get_multilingual_greeting("Bob", language='french') == "Bonjour Bob"
    assert get_multilingual_greeting("Bob", language='swahili') == "I don't speak that language"

def test_perfect_numbers():
    from perfect_numbers import find_perfect_numbers
    assert find_perfect_numbers(8128) == [6, 28, 496, 8128]
    assert find_perfect_numbers(5) == []

def test_triple_finder():
    from triple_finder import find_triples

    assert find_triples([2, 4, 7, 2, 1, 5, 5, 5]) == True
    assert find_triples([2, 4, 7, 2, 1, 2, 2, 6]) == False
    assert find_triples([]) == False

def test_unigram_train():
    from unigram_probability import train_unigram_model

    data = ['fish', 'dog', 'cat', 'frog', 'cat']
    fitted_model = train_unigram_model(data)
    assert fitted_model == {'fish': 1/5, 'dog': 1/5, 'cat': 2/5, 'frog': 1/5}

def test_unigram_score():
    from unigram_probability import score_sentence

    model = {'fish': 1/5, 'dog': 1/5, 'cat': 2/5, 'frog': 1/5}
    sentence = ['fish', 'cat', 'frog']

    assert score_sentence(model, sentence) == pytest.approx(0.016)
