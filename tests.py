"""
Ten moduł zawiera przykładowe funkcje i testy, aby sprawdzić działanie GitHub Actions.
"""


def add(a, b):
    """
    Dodaje dwie liczby.

    Przykład (testowany przez --doctest-modules):
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


def is_palindrome(text):
    """
    Sprawdza, czy tekst jest palindromem.

    Przykład:
    >>> is_palindrome("kajak")
    True
    >>> is_palindrome("hello")
    False
    """
    clean_text = str(text).lower().replace(" ", "")
    return clean_text == clean_text[::-1]


# --- Sekcja testów pytest (funkcje zaczynające się od test_) ---

def test_add_simple():
    """Testuje dodawanie liczb całkowitych."""
    assert add(10, 5) == 15
    assert add(0, 0) == 0


def test_add_floats():
    """Testuje dodawanie liczb zmiennoprzecinkowych."""
    assert add(0.1, 0.2) == 0.1 + 0.2


def test_palindrome_true():
    """Testuje przypadki, które są palindromami."""
    assert is_palindrome("Kajak") is True
    assert is_palindrome("Ada bada") is True  # Ignoruje spacje i wielkość liter


def test_palindrome_false():
    """Testuje przypadki, które NIE są palindromami."""
    assert is_palindrome("Python") is False
    assert is_palindrome(123) is False


if __name__ == "__main__":
    # Pozwala uruchomić testy lokalnie, jeśli nie masz zainstalowanego pytest
    import doctest

    doctest.testmod()
    print("Doctesty przeszły pomyślnie (jeśli brak błędów powyżej).")