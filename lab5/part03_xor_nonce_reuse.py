# Lab 05
# In this python script you will read in 2 ciphertext files and one
# known plaintext file.  The ciphertext files have been generated using 
# two different plaintext files but the same key and the same nonce.
#
# By XORing the two ciphertext files, you will get the same result as 
# just XORing the two plaintext files.
#
# By XORing the resulting XOR of the two plaintext files with the known plaintext 
# (plaintext1),you will recover the original plaintext2.
#
# The syntax to run the python script is 
#
# python3 part03_xor_nonce_reuse.py <cipherTextFile1> <cipherTextFile2> <knownPlainTextFile> <recoveredPlainTextFile>")

import sys
from typing import Tuple

# Read file as binary
# Using typing this says read the filename in as a string and return bytes since you want binary
def readFile(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        return file.read()

# Write data to a file as binary
def writeFile(filename: str, data: bytes) -> None:
    with open(filename, 'wb') as file:
        file.write(data)

# XOR two byte sequences
# This was implemented for you.
# byteSeq1 and byteSeq2 are two files which have been read in as binary data.
# You will use this function to XOR the two ciphertext files 
# and you will use this function to XOR the result of the two ciphertext files with
# the known plaintext file.
# The zip function reads in two byte sequences and pairs up the corresponding elements.
# a ^ b is the XOR function.  As it is implemented, for each byte it performs an XOR
# of the two corresponding bits.

def xorBytes(byteSeq1: bytes, byteSeq2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(byteSeq1, byteSeq2))

# Main function to perform XOR operations to recover plaintext
def main() -> None:
    # Check command line arguments
    if len(sys.argv) < 5:
        print("Usage:")
        print("  python3 part03_xor_nonce_reuse.py <cipherTextFile1> <cipherTextFile2> <knownPlainTextFile> <recoveredPlainTextFile>")
        sys.exit(1)

    # TODO:  Read in the filenames from command line arguments
    cipherTextFile1 = sys.argv[1]
    cipherTextFile2 = sys.argv[2]
    plainText = sys.argv[3]
    plainTextRecovered = sys.argv[4]

    # TODO:  Read the two ciphertext files and the known plaintext file using the readFile function
    cipherText1 = readFile(cipherTextFile1)
    cipherText2 = readFile(cipherTextFile2)
    plainTextGiven = readFile(plainText)

    # TODO:  XOR the two ciphertexts to obtain the XOR of the plaintexts using the xorBytes function
    xorPlainTexts = xorBytes(cipherText1, cipherText2)

    # TODO:  XOR the above ciphertext result with the known plaintext 
    #        This recovers the second plaintext/
    #        Again use the xorBytes function.
    plainTextRecovered2 = xorBytes(xorPlainTexts, plainTextGiven)

    # TODO:  Write the recovered plaintext to the output file using the writeFile function
    writeFile(plainTextRecovered, plainTextRecovered2)

    # Print the recovered plaintext in ASCII (if possible)
    try:
        print(f"Recovered Plaintext 2 (ASCII): {plainTextRecovered2.decode('ascii')}")
    except UnicodeDecodeError:
        print("Warning: The recovered plaintext contains non-ASCII characters and could not be fully decoded as ASCII.")
        print(f"Recovered plaintext written to '{plainTextRecovered}'.")

# Entry point
if __name__ == "__main__":
    main()