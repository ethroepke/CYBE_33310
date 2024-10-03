# Lab 05
# In this lab you will encrypt and decrypt a file using a provided 
# key and nonce.  The input and output files need to be read and written 
# as binary files. 
#
# Typing is used to help you understand the functions.   
#
# The syntax to run the python script is 
#
# Encrypt 
#    python3 part01_encrypt_decrypt_chacha_skel.py encrypt <inputFile> <outputFile> <keyFile> <nonceFile>
#
# Decrypt 
#    python3 part01_encrypt_decrypt_chacha_skel.py decrypt <inputFile> <outputFile> <keyFile> <nonceFile>   

import os
import sys
from typing import Tuple
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Read file as binary
# Using typing this says read the filename in as a string and return bytes since you want binary
def readFile(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        return file.read()

# Write data to a file as binary
def writeFile(filename: str, data: bytes) -> None:
    with open(filename, 'wb') as file:
        file.write(data)

# Read key/nonce from their respective files
def loadKeyNonce(keyFilename: str, nonceFilename: str) -> Tuple[bytes,bytes]:
    #TODO:  Read the key and nonce values into their respective variables using the readFile function 
    key = readFile(keyFilename)
    nonce = readFile(nonceFilename)
    return key, nonce

# Encrypt data using ChaCha20
#
# The following lines use the Cipher class to create an instance of encryption operation.
# It has to be configured with the correct encryption algorithm, mode, and backend.
# Below you are creating a Cipher object that uses ChaCha20 with the key and nonce you read in from their files.
# The backend just handles the cryptographic operations for you.
# The encryptor is an object that performs the encryption on the data provided. 
# The update method returns the ciphertext.
def chacha20Encrypt(data: bytes, key: bytes, nonce:bytes) -> bytes:
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data)

# Decrypt data using ChaCha20
#
# Similar to the encrypt function, you create the Cipher object and tell it to use ChaCha20, key, and nonce.
# Again the backend handles the cryptographic operations for you.
# The decryptor object takes the binary file containing the encrypted message and using the same key and nonce, 
# transforms it back to the original plaintext.   
def chacha20Decrypt(data: bytes, key: bytes, nonce:bytes) -> bytes:
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data)

# Main function can either encrypt or decrypt using ChaCha20
def main():
    # Check command line arguments
    if len(sys.argv) < 6:
        print("Usage:")
        print("  Encryption: python3 part01_encrypt_decrypt_chacha_skel.py encrypt <inputFile> <outputFile> <keyFile> <nonceFile>")
        print("  Decryption: python3 part01_encrypt_decrypt_chacha_skel.py decrypt <inputFile> <outputFile> <keyFile> <nonceFile>")
        sys.exit(1)

    # TODO:  Read in the operation (encrypt/decrypt), inputFile, outputFile, keyFile, and nonceFile from the command line
    # using sys.argv[].
    #
    # You will probably want to use .lower on the operation just in case someone uses all uppercase or mixed case Encrypt or Decrypt.
    operation = sys.argv[1].lower()
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
    keyFile = sys.argv[4]
    nonceFile = sys.argv[5] 

    if operation == 'encrypt': 
        # TODO:  Read the plainText file using the readFile function
        plainText = readFile(inputFile)

        # TODO:  Load key and nonce from binary files provided using the loadKeyNonce function
        key, nonce = loadKeyNonce(keyFile, nonceFile)

        # TODO:  Encrypt the plainText using the chacha20Encrypt function.
        cipherText = chacha20Encrypt(plainText, key, nonce)

        # TODO:  Write the cipherText to the outputFilename using the writeFile function.  
        writeFile(outputFile, cipherText)

        print(f"File '{inputFile}' encrypted successfully to '{outputFile}'.")

    elif operation == 'decrypt':
        # TODO:  Load key and nonce from files using the loadKeyNonce function
        key, nonce = loadKeyNonce(keyFile, nonceFile)

        # TODO:  Read the input (encrypted) file using the readFile function
	encryptedData = readFile(inputFile)

        # TODO:  Decrypt the data using the chacha20Decrypt function
        decryptedText = chacha20Decrypt(encryptedData, key, nonce)

        # TODO:  Write the plainText to the outputFilename using the writeFile function.
        writeFile(outputFile, decryptedText)

        print(f"File '{inputFile}' decrypted successfully to '{outputFile}'.")

        # Print the decrypted content in ASCII format to check if you properly decrypted
        try:
            print(f"Decrypted content (ASCII): {decryptedText.decode('ascii')}")
        except UnicodeDecodeError:
            print("Warning: The decrypted content contains non-ASCII characters and could not be fully decoded as ASCII.")


    else:
        print("Invalid operation. Please use 'encrypt' or 'decrypt'.")
        sys.exit(1)

# Entry point
if __name__ == "__main__":
    main()