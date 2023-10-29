
print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg= input("ENTER YOUR MESSAGE: ")
    key = int(input("Enter Key for encryption :"))
    
    encrypted_text = ""

    for i in range(len(msg)):
        char = ord(msg[i]) + key 
        if char>126:
            char = char - 127 + 32
            
        encrypted_text += chr(char)

    print('ENCRYPTED TEST IS:', encrypted_text)

def decryption():
    print("Decryption")

    encripted_msg = input("Enter encrypted text :")
    decrypted_key = int(input("Enter key (1-94) :"))
    
    decrypted_text = ""

    for i in range(len(encripted_msg)):
        char = ord(encripted_msg[i]) + decrypted_key 
        if char < 32 :
            char = char + 127 - 32
            
        decrypted_text += chr(char)

    print('DECRYPTED TEXT IS:', decrypted_text)


       
if __name__ == "__main__":
    main()