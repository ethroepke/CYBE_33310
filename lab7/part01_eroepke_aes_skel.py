# Lab 07 part 01
# You will be implementing AES encryption and decryption.
# This code is a client that should be able to communicate
# with a server I am running in iselab.  You are not responsible
# for the socket and network connections.  Those are provided.
# You will be responsible for implementing the cryptographic functions
# of encrypt and decrypt in CBC mode.  
#
# The client will read a plaintext message and AES key from the provided
# files.  You will encrypt the message using AES and send it to the server.
# The server will decrypt the message and return it to you to verify that 
# your encryption worked properly.
# Then the server will provide an encrypted message that you will have to decrypt.
# Both are already setup to display on the terminal for you.

# Syntax:  python3 part01_aes_student_skel.py part01_key_encrypt part01_plaintext.txt  part01_plaintext_outfile.txt


import socket
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom
import struct

# Pad the plaintext to 16 bytes which is the AES block size
def padMessage(message: bytes)-> bytes:
    paddingLength = 16 - len(message) % 16
    return message + bytes([paddingLength] * paddingLength)

# Unpad the decrypted plaintext
def unpadMessage(paddedMessage: bytes)-> bytes:
    paddingLength = paddedMessage[-1]
    return paddedMessage[:-paddingLength]

# AES encryption function
def encryptMessage(key: bytes, plaintext: bytes) -> bytes:
    # Generate a random IV (16 bytes). It must be unique for each message.
    iv = urandom(16) 
    # TODO:  use https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    # to determine how to replace the XXX values.  You will use CBC as your block cipher mode.
    # Chose this, use AES algorithm and CBC mode with the generated IV
    #Found under section for symmetric encryption in website
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    #Encrypt the cipher line above this
    encryptor = cipher.encryptor()
    paddedPlaintext = padMessage(plaintext)
    ciphertext = encryptor.update(paddedPlaintext) + encryptor.finalize()
    # Prepend the IV to the ciphertext
    return iv + ciphertext

# AES decryption function
def decryptMessage(key: bytes, ciphertext: bytes) -> bytes:
    # Extract the IV which is the first 16 bytes
    iv = ciphertext[:16]  
    # TODO:  use https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
    # to determine how to replace the XXX values.  You will use CBC as your block cipher mode.
    #Chose this, use AES and mode CBC with IV extracted
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decryptedMessage = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    # Remove padding after decryption    
    return unpadMessage(decryptedMessage)  

def sendWithSize(conn: socket.socket, message: bytes) -> None:
    # Send the size of the message first (packed as 4 bytes)
    # 4-byte unsigned int in network byte order
    messageSize = struct.pack('!I', len(message))  
    conn.sendall(messageSize)
    # Send the actual message
    conn.sendall(message)

def recvWithSize(conn: socket.socket)-> bytes:
    # Receive the message size first (4 bytes)
    messageSizeData = conn.recv(4)
    if not messageSizeData:
        return None
    messageSize = struct.unpack('!I', messageSizeData)[0]
    
    # Now receive the full message
    receivedMessage = b''
    while len(receivedMessage) < messageSize:
        packet = conn.recv(min(messageSize - len(receivedMessage), 1024))
        if not packet:
            # Return None if the connection is closed or interrupted
            return None  
        receivedMessage += packet
    return receivedMessage

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 part01_aes_student_skel.py part01_key_encrypt part01_plaintext.txt  part01_plaintext_outfile.txt")
        sys.exit(1)

    # Extracting file names from argv[]
    keyFileName = sys.argv[1]
    messageFileName = sys.argv[2]
    outputFileName = sys.argv[3]

    # Socket connection
    # My server IP address using an ephemeral port
    HOST = '34.18.12.211'
    PORT = 65432

    # Read the AES key from a file
    with open(keyFileName, 'rb') as keyFile:
        # Key is 16 bytes for AES-128
        key = keyFile.read().strip()  


    # Read the plaintext message from a file
    with open(messageFileName, 'rb') as messageFile:
        message = messageFile.read().strip()

    # Get NetID from the student for screenshot
    netID = input("Enter your NetID: ").strip()

    # Encrypt the message
    encryptedMessage = encryptMessage(key, message)

    # Connect to the server and send the NetID and encrypted message
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Send NetID to the server as UTF-8
        s.sendall(netID.encode())  

        # Send the encrypted message (IV + ciphertext)
        sendWithSize(s, encryptedMessage)

        # Receive the decrypted message from the server to show your encryption was valid
        decryptedMessage = recvWithSize(s)  

        if decryptedMessage is None:
            print("Error: Did not receive a decrypted message from the server.")
            sys.exit(1)

        print(f"Decrypted message from server: {decryptedMessage.decode()}")

        # Save the decrypted message to a file
        with open(outputFileName, 'wb') as decryptedFile:
            decryptedFile.write(decryptedMessage)

        # Receive a new encrypted message from the server (IV + ciphertext)
        encryptedMessageFromServer = recvWithSize(s)

        if encryptedMessageFromServer is None:
            print("Error: Did not receive an encrypted message from the server.")
            sys.exit(1)

        # Decrypt the message from the server (IV + ciphertext)
        decryptedMessageFromServer = decryptMessage(key, encryptedMessageFromServer)
        print(f"Decrypted message from server to decrypt: {decryptedMessageFromServer.decode()}")

if __name__ == "__main__":
    main()
