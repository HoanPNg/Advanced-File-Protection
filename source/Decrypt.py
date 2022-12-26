from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

import helper
import os

def decrypt(cipherTxt,password,iv):
    # Password hashing
    pwHash = SHA256.new(password.encode())
    pwHash2 = SHA256.new((pwHash.hexdigest()).encode())

    # create new AES object
    key =  pwHash2.digest()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher

    # Decrypt
    original_data = unpad(cipher.decrypt(cipherTxt), AES.block_size) # Decrypt and then up-pad the result
    return original_data