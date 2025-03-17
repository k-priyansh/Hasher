# pip install cryptography
from cryptography.fernet import Fernet

# encrypter function
def encrypt_text(text,key):
    f = Fernet(key)
    token = f.encrypt(text.encode())
    return token


# decrypter function
def decrypt_text(encrypted_token,key):
    f = Fernet(key) 
    decrypted_text = f.decrypt(encrypted_token).decode()
    print("Decrypted text:", decrypted_text)
    return decrypted_text

# option
print('select the option from the given below: ')
print("1. encrypt") 
print("2. decrypt")
option=int(input("enter option: "))



if option == 1:
    # encrypt
    # generating the key
    key = Fernet.generate_key()
    print("key: ",key)
    # text
    text = input("Enter text: ")
    # calling encrypter function
    encrypted_text = encrypt_text(text, key)
    print("Encrypted text:", encrypted_text)
elif option == 2:
    # key
    key = input("Enter key: ")
    # encrypted text
    encrypted_token = input("Enter encrypted token: ")
    # calling decrypter function
    decrypt_text(encrypted_token, key)
else:
    print("Wrong option selected")
