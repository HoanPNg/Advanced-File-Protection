from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
import random
import helper
import os


def encrypt(plain_text, password):
    # create key
    pwHash = SHA256.new(password.encode())
    pwHash2 = SHA256.new((pwHash.hexdigest()).encode())
    key =  pwHash2.digest()
    
    # pad message
    if type(plain_text) == str:
        plain_text = plain_text.encode()
    pad_plain_text = pad(plain_text, AES.block_size)

    # Create AES object
    cipher = AES.new(key, AES.MODE_CBC) 
    ciphered_data = cipher.encrypt(pad_plain_text) 

    headPad = os.urandom(15)
    lenTailPad = random.randint(5,250)
    
    # RETURN 
    return ciphered_data, cipher.iv

