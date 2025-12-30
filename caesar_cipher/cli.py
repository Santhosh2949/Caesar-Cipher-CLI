import argparse
from caesar_cipher.core import caesar

def validate_text(text: str ) -> None:
    
    if not all(ch.isalpha() or ch.isspace() for ch in text):
        raise ValueError("Text must contain only letters and spaces")
         


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Command Line Tool")

    parser.add_argument("-t", "--text",required=True,help="Text to encrypt or decrypt (letters and spaces only)")

    parser.add_argument("-s", "--shift",type=int,required=True,help="Shift value (integer)")

    parser.add_argument("-d", "--decrypt",action="store_true",help="Decrypt instead of encrypt")

    args = parser.parse_args()

    try:
        validate_text(args.text)
    except ValueError as e:
        parser.error(str(e))

    result = caesar(args.text,args.shift,encrypt=not args.decrypt)

    print(result)