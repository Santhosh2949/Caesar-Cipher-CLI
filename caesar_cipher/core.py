def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(shift, int):
        raise TypeError("shift must be an integer")
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift %= 26

    if not encrypt:
        shift = -shift

    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet + alphabet.upper(),shifted + shifted.upper())

    return text.translate(table)
