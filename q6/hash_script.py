import hashlib
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 hash_script.py <your password>")
    else:
        password = bytes(sys.argv[1], 'utf-8')
        salt = bytes('Km5d5ivMy8iexuHcZrsD', 'utf-8')
        hash = hashlib.pbkdf2_hmac(
            'sha512', password, salt, 200000)
        print(hash.hex())
