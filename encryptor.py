from cryptography.fernet import Fernet
import base64
import os

key = base64.urlsafe_b64encode(os.urandom(32))

enc = Fernet(key)

encMessage = enc.encrypt("suck my cock".encode())
decMessage = enc.decrypt(encMessage).decode()

print(decMessage)

def setKey(key):
    enc = Fernet(key)

def encryptMessage(message):
    return enc.encrypt(message.encode())

def decryptMessage(message):
    return enc.decrypt(message).decode()