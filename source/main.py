from Encrypt import encrypt
from Decrypt import decrypt
import helper
import gui

def run():
    option = -1
    while option != 0:
        gui.printMenu()
        option = int(input("Enter your option: "))

        # Encrypt ===================
        if option == 1:
            fileName = input("Enter file's name: ")
            data = helper.readFile(fileName)
            if data == None:
                continue
            else:
                password = ""

                while True: 
                    password = input("Enter your password: ")
                    if helper.passwordConfirm(password):
                        break
                    else:
                        "Password invalid"
                
                EncData, IV = encrypt(data, password);
                helper.writeFileWithRandom("R_E" +fileName, EncData,IV)
                
        # Decrypt ===================
        if option == 2:
            fileName = input("Enter file's name: ")
            data = helper.readFileWithRandom(fileName)
            if data == None:
                continue
            else:
                password = input("Enter password: ")
                iv = data[-16:]
                cipher = data[:-16]

                original = decrypt(cipher,password,iv)

                _ = helper.writeDncFile("R_D"+fileName,original)
                
                    
run()

                

    

