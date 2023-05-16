import time

class CesarCipher():
    def __init__(self) -> None:
        self.__key = 0
        self.__text = ""
    def cipher(self):
        self.__text_cipher = ""

        try:
            print("\n[---- CIPHER ----]")
            self.__text = str(input("Enter the text to encrypt: "))
            self.__key = int(input("Enter the key: "))

            print("\n[+]Starting encription....")
            time.sleep(1)
            print("[+]Plain Text: " + self.__text)
            print("[+]Key: " + str(self.__key))

            for x in self.__text:
                self.__text_cipher += chr(ord(x) + self.__key % 95)

            print("[+]Text Cipher: " + self.__text_cipher)
            input()

        except ValueError:
            print("[-]The entered value is incorrect. Press any key to go back.")
            input()

    def decipher(self):
        self.__text_decipher = ""

        try:
            print("\n[---- DECIPHER ----]")
            self.__text = str(input("Enter the text to encrypt: "))
            self.__key = int(input("Enter the key: "))

            print("\n[+]Starting decryption...")
            time.sleep(1)
            print("[+]Text Cipher: " + self.__text)
            print("[+]Key: " + str(self.__key))

            for x in self.__text:
                self.__text_decipher += chr(ord(x) - self.__key % 95)

            print("[+]Text Decipher: " + self.__text_decipher)
            input()
            
        except ValueError:
            print("[-]The entered value is incorrect. Press any key to go back.")
            input()

def main():
    option = 0

    while(option != 3):

        try:
            print("""
   ___                     ___ _      _            
  / __|___ ___ __ _ _ _   / __(_)_ __| |_  ___ _ _ 
 | (__/ -_|_-</ _` | '_| | (__| | '_ \ ' \/ -_) '_|
  \___\___/__/\__,_|_|    \___|_| .__/_||_\___|_|  
                                |_| 
    Created by: @odindaza
            """)
            print("1. Cipher")
            print("2. Decipher")
            print("3. Exit")

            option = int(input("\n>>> "))
            caesar_cipher = CaesarCipher()

            if(option == 1):
                caesar_cipher.cipher()
            elif(option == 2):
                caesar_cipher.decipher()
            elif(option == 3):
                break
            else:
                print("[-]The selected option is incorrect")
                option = 0
        except ValueError:
                print("[-]The entered value is incorrect. Press any key to go back.")
                input()

if __name__ == "__main__":
    main()