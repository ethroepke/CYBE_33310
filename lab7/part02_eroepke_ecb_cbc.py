# Lab 07 part 02
# You will explore how AES encryption works in different modes.  In this program you will
# specifically look at ECB (Electronic Codebook) and CBC (Cipher Block Chaining)
#
# BMP files have a clear structure differentiating between header information
# and the pixel data.  This allows you to visually see the effect of encryption
# on the image, especially how different modes either preserve or hide patterns
# in the image.
#
#
# Syntax:  python3 part02_ecb_cbc_skel.py part02_input_bmp.bmp part02_output_ecb_bmp.bmp part02_output_cbc_bmp.bmp


import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

# Function to encrypt pixel data using AES in ECB mode
def encryptEcb(key: bytes, data: bytes) -> bytes:
    # TODO:  use https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    # to determine how to replace the XXX values.  You will use ECB as your block cipher mode.
    #Found under insecure modes, Use AES with ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    # Encrypt line above with encryptor method
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

# Function to encrypt pixel data using AES in CBC mode
def encryptCbc(key: bytes, data: bytes) -> bytes:
    # Generate random IV for CBC mode
    # Notice you didn't do this for ECB above
    iv = urandom(16)  
    # TODO:  use https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    # to determine how to replace the XXX values.  You will use CBC as your block cipher mode.
    # Function name states encrypting CBC so using CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Prepend the IV
    return iv + (encryptor.update(data) + encryptor.finalize())  

# Read the BMP file (separate header and pixel data)
def readBmp(filePath: str) -> tuple:
    with open(filePath, 'rb') as f:
        # BMP header
        header = f.read(54) 
           # Now read the pixel data you will encrypt
        data = f.read()  
    return header, data

# Write the encrypted BMP file (header + encrypted pixel data)
def writeBmp(filePath: str, header: bytes, data: bytes) -> None:
    with open(filePath, 'wb') as f:
        # Write the BMP header
        f.write(header)  
        # Write the encrypted pixel data
        f.write(data)  

# Main function to run the encryption and comparison
def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python3 part02_ecb_cbc_skel.py part02_input_bmp.bmp part02_output_ecb_bmp.bmp part02_output_cbc_bmp.bmp")
        sys.exit(1)

    inputBmpFile = sys.argv[1]
    outputEcbFile = sys.argv[2]
    outputCbcFile = sys.argv[3]

    # Generate AES-128 key which is 16 bytes long
    key = urandom(16)  

    # Read the BMP file
    header, pixelData = readBmp(inputBmpFile)

    # Pad pixel data to multiple of AES block size (16 bytes)
    paddingLength = 16 - (len(pixelData) % 16)
    pixelData += bytes([paddingLength] * paddingLength)

    # Encrypt in ECB mode
    encryptedEcb = encryptEcb(key, pixelData)
    writeBmp(outputEcbFile, header, encryptedEcb)

    # Encrypt in CBC mode
    encryptedCbc = encryptCbc(key, pixelData)
    writeBmp(outputCbcFile, header, encryptedCbc)

    print("Encryption complete. Check the encrypted BMP files.")

if __name__ == "__main__":
    main()