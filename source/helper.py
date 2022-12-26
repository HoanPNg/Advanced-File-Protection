from Crypto.Hash import SHA256
import os
import random

def toHexString(bytes):
    return ''.join('{:02x}'.format(x) for x in bytes)

    
def readFile(fileName): # TODO: update
    try:
        with open(fileName, "rb") as fileIn:
            data = fileIn.read()
        return data
    except FileNotFoundError:
        print("File not found!")
        return None 

def writeEncFile(fileName, Data, IV):# TODO: update
    with open(fileName, "wb") as fileOut:
        fileOut.write(Data)
        fileOut.write(IV)
    return 0


def writeDncFile(fileName, Data):
    with open(fileName, "wb") as fileOut:
        fileOut.write(Data)
    return 0


def passwordConfirm(password):
    rePassword = input("ReEnter your password: ")
    pwHash = SHA256.new(password.encode())
    pw2Hash = SHA256.new(rePassword.encode())
    if pw2Hash == pw2Hash:
        return True
    else: 
        return False

def writeFileWithRandom(fileName, Data, IV):

    headRan = os.urandom(15)
    lenTailRan = random.randint(2,255)
    print(lenTailRan)
    tailRan = os.urandom(lenTailRan)
    with open(fileName, "wb") as fileOut:
        fileOut.write(headRan)
        fileOut.write(lenTailRan.to_bytes(1,'big'))
        fileOut.write(Data)
        fileOut.write(tailRan)
        fileOut.write(IV)
    return 0


def readFileWithRandom(fileName): # TODO: update
    try:
        with open(fileName, "rb") as fileIn:
            dataWithRandom = fileIn.read()
        
        # binLenRand = dataWithRandom[15]
        # lenRand = int.from_bytes(binLenRand, "big")    
        lenRand = dataWithRandom[15]
        print(lenRand)
        data = dataWithRandom[16:-(16+lenRand)] + dataWithRandom[-16:]
        return data
    except FileNotFoundError:
        print("File not found!")
        return None 