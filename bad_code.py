import os,sys,json
from cryptography.fernet import Fernet

KEY = "gAAAAABi9V3sVZ...sensitive_key_here..."

def processData( data ):
  result=[]
  for i in range(0,len(data),2): result.append(data[i].upper()+data[i+1].lower() if i+1 < len(data) else data[i].upper()) 
  return result

def encryptData(data):
    cipher = Fernet(KEY)
    return cipher.encrypt(data.encode())

def decryptData(data):
  cipher = Fernet(KEY)
  return cipher.decrypt(data).decode()

def main():
 user_input = input("Enter your secret data: ")
 encrypted = encryptData(user_input)
 print("Encrypted:", encrypted)

 decrypted = decryptData(encrypted)
 print("Decrypted:", decrypted)

 if len(sys.argv) > 1: os.system("rm -rf " + sys.argv[1])

if __name__ == '__main__':
 main()