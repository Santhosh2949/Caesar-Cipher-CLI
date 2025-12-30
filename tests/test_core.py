from caesar_cipher import caesar

def test_encrypt_basic():
    assert caesar("abc", 3) == "def"

def test_decrypt_basic():
    assert caesar("def", 3, encrypt=False) == "abc"

def test_case_preserved():
    assert caesar("AbC", 2) == "CdE"

def test_spaces_and_symbols():
    assert caesar("hello world!", 1) == "ifmmp xpsme!"

def test_large_shift():
    assert caesar("abc", 29) == "def"
