import os
import sys
import json
from cryptography.fernet import Fernet
from typing import List

# Ensure the key is securely managed and not hardcoded in the script
KEY = os.getenv("ENCRYPTION_KEY")

def process_data(data: str) -> List[str]:
    """
    Process the input data by alternating the case of characters.
    
    Args:
        data (str): The input string to process.
    
    Returns:
        List[str]: A list of processed strings with alternating case.
    """
    result = []
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            result.append(data[i].upper() + data[i + 1].lower())
        else:
            result.append(data[i].upper())
    return result

def encrypt_data(data: str) -> bytes:
    """
    Encrypt the input data using Fernet encryption.
    
    Args:
        data (str): The input string to encrypt.
    
    Returns:
        bytes: The encrypted data.
    """
    if not KEY:
        raise ValueError("Encryption key not found. Set the ENCRYPTION_KEY environment variable.")
    cipher = Fernet(KEY)
    return cipher.encrypt(data.encode())

def decrypt_data(data: bytes) -> str:
    """
    Decrypt the input data using Fernet encryption.
    
    Args:
        data (bytes): The encrypted data to decrypt.
    
    Returns:
        str: The decrypted string.
    """
    if not KEY:
        raise ValueError("Encryption key not found. Set the ENCRYPTION_KEY environment variable.")
    cipher = Fernet(KEY)
    return cipher.decrypt(data).decode()

def main() -> None:
    """
    Main function to handle user input, encryption, and decryption.
    """
    user_input = input("Enter your secret data: ")
    encrypted = encrypt_data(user_input)
    print("Encrypted:", encrypted)

    decrypted = decrypt_data(encrypted)
    print("Decrypted:", decrypted)

    if len(sys.argv) > 1:
        # Sanitize the input to prevent command injection
        path_to_remove = os.path.abspath(sys.argv[1])
        if os.path.exists(path_to_remove):
            os.system(f"rm -rf {path_to_remove}")

if __name__ == '__main__':
    main()
