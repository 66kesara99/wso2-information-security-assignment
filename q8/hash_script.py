import hashlib
import sys
import os

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 hash_script.py <your password>")
    else:
        password = bytes(sys.argv[1], 'utf-8')
        salt = os.urandom(20)
        hash = hashlib.new('sha512')
        hash.update(password)
        hash.update(salt)
        print(hash.hexdigest())
