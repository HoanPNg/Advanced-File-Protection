# Advanced-File-Protection
## General:
This is a small project for Data Safety and Recovery course at HCMUS. The goal is to create a encryption program that has radomness (so that only the creator can decrypt).

## Requirement:
- Pycryptdomex library:
``` 
pip install pycryptodomex --no-binary :all: 
```
## Design:
<img src="./img/Structure.png" alt="Encrypted file structure">

### Random:
- 15 random bytes
### int:
- random generated 1 byte int, contains the length of Random 2 part
### Encryted Data:
- Data of the file that has been encrypted using AES-256 with CBC mode
- encryption's key is generated from user's password using double SHA256
$$key=SHA256(SHA256(password))$$
### Random 2
- Random bytestream with the length 'int' 
### IV 
- Random generated from key's generation.
- Used for decrypt

    
## Features:
- Secure encryption with AES-256.
- Password is not stored on the system and is hashed with SHA-256.
- Size and content of ecnrypted file is diffence for each time encrypt.

## Author:
Phan Ngoc Hoan
