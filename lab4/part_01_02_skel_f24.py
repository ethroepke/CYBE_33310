# Lab 04  :

#This program will have two options to work with a LFSR cryptosystem 
#  1) Encrypt or Decrypt
#  2) Cryptanalysis
#  The simplest way to accomplish this is to reuse the functions
#
#  It is also easiest if you put filenames on the command line
#  For example: 
#         python3 part01_02.py input_file output_file
#  1) Encrypt - inputFile == plaintext, outputFile == ciphertext
#  2) Decrypt - inputFile == ciphertext, outputFile == plaintext
#  3) Cryptanalysis - inputFile_1 == knownplaintext, inputFile_2 == ciphertext, 
#     outputFile == possiblekeystream

import sys
import numpy
import base64

def readFile(filename: str, fileType) -> numpy.array:
     """_summary_ Read the file from filename, and return the data in the file.
          Read it in the entire file to memory as a single string using file.read()
          Convert the characters to their ASCII values and store them in a numpy array
          Unpack the ASCII characters into bits using little endian ordering
          Return the numpy array of bits 

     Args:
         filename (str): _description_ The name of the file to read from

     Returns:
         numpy.array: _description_ The array of data (bits) read from the file
     """

     #Read file in binary because we are workin in bits (less code we have ti write)
     with open(filename, 'rb') as file:
         fileContent = file.read()

     # Create a list to store the characters or binary data in
     returnList = numpy.frombuffer(fileContent, dtype=numpy.uint8)

     #convert the characters to their ASCII value and store them in array
     #for byte in fileContent:
         #returnList = numpy.append(returnList, byte)

     #unpack the ASCII characters into bits using little endian
     bitArray = numpy.unpackbits(returnList, bitorder='little')

     # TODO:
     # Open the file with file.read()
     # Use numpy.array to create a numpy.array that holds the ascii values for the 
     #   characters that have been read.
     #   example syntax:  numpy.array([ord(c) for c in filename], dtype=numpy.uint8)
     # Unpack the bits in the ascii character array, be sure to use little endian.
     #   example syntax:  numpy.unpackbits(characterArray, bitorder='little')
     # Return the list by appending the bits
     #   example syntax:  numpy.append(list,bits)
     # I am giving you part of the file.read() syntax because you need to identify between 
     # ascii and binary files. plaintext will be ascii.  keystream and ciphertext will be binary.

     if fileType == 'binary':
          with open (filename, 'r') as file:
               base64Data = file.read()
               binaryData = base64.b64decode(base64Data)
               packedData = numpy.frombuffer(binaryData, dtype=numpy.uint8)
               readBits = numpy.unpackbits(packedData, bitorder = 'little')

     elif fileType == 'ascii':
          with open (filename, 'r', encoding ='ascii') as file:
               fileChars = file.read()
               charAscii = numpy.array([ord(c) for c in fileChars], dtype=numpy.uint8)
               readBits = numpy.unpackbits(charAscii, bitorder='little')
     else:
          raise ValueError("fileType must be either 'binary' or 'ascii'")

     return bitArray # return the list you generated 
 


def writeFile(filename: str, data, fileType):
     """_summary_ Write the data to the file with the given filename.
          This can be used to save out the cipherText, the plainText, or the keyStream.
          A potential way to do this is to pack 8 bits into a single byte and write
          that byte out to the file.

     Args:
         filename (_type_): _description_ The name of the file to write to.
         data (_type_): _description_ The data to write to the file.
     """
     # TODO:
     # Write out ascii characters to a file with file.write()
     # Pack the bits created and use little endian
     #    example syntax:  numpy.packbits(data, bitorder='little')
     # For each byte create an ascii character
     #    example syntax:  "".join(chr(byte) for byte in packedData)
     # I am giving you the file.write() syntax because you need to know 
     # whether you are writing to a binary file or an ascii file.
     # plaintext will be ascii.  keystream and ciphertext will be binary.
     if fileType == 'binary':
         packedData = numpy.packbits(data, bitorder='little')
base64Data = base64.b64encode(packedData).decode('ascii')
         with open (filename, 'w') as file:
              file.write(base64Data)

     elif fileType == 'ascii':
          packedData = numpy.packbits(data, bitorder='little')
          asciiData = ''.join(chr(byte) for byte in packedData)
          with open (filename, 'w') as file:
               file.write(asciiData)

     else:
          raise ValueError("fileType must be either 'binary' or 'ascii'")



def cycle(register):
     """_summary_ Run an LFSR on a 4-bit register, and return the result
               of the LFSR on the input register. This will place the new
               bit in the 4th  position of the register (index 0), and shift all other
               bits left, dropping bit 1 (index 3).

               **************** 
               The logic will change for part 02 of the lab.  You will
               have to determine which registers are used and modify the 
               function.  You must include the logic for BOTH part 01 and 02 
               in the code with part 01 commented.  
               ***************

     Args:
          register (str, int): _description_ Register to run the LFSR on
               this can be a string containing the binary representation of the
               register, or an integer containing the decimal representation of
               the register.

     Raises:
          ValueError: _description_ If the input is not 4 bits or less
               this error will be raised.

     Returns:
          _type_: _description_ The result of running the LFSR on the input
               register. This will be returned as a numpy array of bits.
     """
    
     if(len(register) != 4):
          raise ValueError("numpy.ndarray length must be 4 bits or less")
     registerBits = numpy.array([int(bit) for bit in register], dtype=numpy.uint8)

     #XOR first and last bits of register
     newValue = numpy.bitwise_xor(registerBits[0], registerBits[3])
    
     #shift register bits
returnVal = numpy.array([newValue, registerBits[0], registerBits[1], registerBits[2]])

     # XOR the first and last bits of the register
     #   example syntax:  numpy.bitwise_xor(bit, bit)
     # Insert the XOR value at index 0, shift all other bits one position right, drop bit at index [3].
     #   example syntax:  numpy.array([newvalue, bit[0], bit[1], bit[2]])
     # Return the new numpy array of bits
     # You will use this function in part 01 and part 02.  You must leave the logic for part 01 in this function
     # and comment it out when running part 02.  You will change the taps for part 02 and have a different seed value.
     # You MUST have both pieces of logic to get full credit.

     return returnVal
 
def makeKeyStream(seedValue: numpy.ndarray, length: int):
     """_summary_ Generate a key_stream of the given length. This is usually the length
          of the plaintext or ciphertext that is being encrypted or decrypted. 

          The key_stream is generated by taking the bit at index 3 of the register [3] in each cycle.
          Don't forget that you must include bit at index 3 of the seed value as the first bit in the keyStream.

     Args:
         seed_value (_type_): _description_ The seed value to start out the key_stream
         length (int): _description_ The number of values that should be generated
                in the keyStream

     Returns:
         _type_: _description_
     """
     #  Create an array to store the keyStream into
     keyStream = numpy.empty(length, dtype=numpy.uint8)
     # TODO:  Use cycle() here to generate the keyStream
     # Remember the bit at index [3] of the register is the first bit in the keyStream.  
     # After that every bit at index [3] is keyStream.

     #Store the first bit of the seed value into keyStream
     keyStream[0] = seedValue[3]

     #loop through remaining length and generate keyStream using Cycle()
     currentRegister = seedValue.copy()
     for i in range(1, length):
         currentRegister = cycle(currentRegister)
         #Take the bit at index 3 at current register and store in keyStream
         keyStream[i] = currentRegister[3]


     return keyStream


def XOR(inputData, keyStream):
     """_summary_ A function that takes in two items, and XORs the bit values of
          each of them together.
This can be used with plaintext and keyStream to encrypt into ciphertext.
          It can also be used with ciphertext and keyStream to decrypt into plaintext.
          Finally, it can be used with knownPlaintext and ciphertext to perform cryptanalysis.

     Args:
         data (_type_): _description_ The data to XOR with the keyStream
         key_stream (_type_): _description_ The keyStream to XOR with the data

     Returns:
         _type_: _description_ The result of XORing the data with the keyStream
     """
     returnBitData = numpy.array([], dtype=numpy.uint8)
     # TODO: 
     # NOTE: It is likely good to implement this in a way that if the length of the two
     #    inputs are not the same, that it returns when the shorter one had every element
     #    used. This will help with cryptanalysis, where knownPlaintext and ciphertext
     #    will not be the same length.
     #    example syntax: numpy.bitwise_xor(inputData, keyStream)

     #Determine length to iterate based on shorter of two index
     minLength = min(len(inputData), len(keyStream))

     #XOR the values and store to returnBitData
     for i in range(minLength):
         xorResult = numpy.bitwise_xor(inputData[i], keyStream[i])
         returnBitData = numpy.append(returnBitData, xorResult)


     return returnBitData



def main():
     # Prompt for action
     action = input("Do you want to 1) encrypt / decrypt or  2) conduct cryptanalysis?")
     try:
          action = int(action)
     except:
          print("Action could not be converted to an integer, please enter 1 or 2")
          return

     if (action == 1):
          # Check for two sys.argv[x]
          if(len(sys.argv) < 3):
               print("Not enough arguments")
               print("Usage: python3 part01_02.py inputFile outputFile keystreamFile")
               return

          # Prompt for starting values: input()
          # Ex: 1001
          inputString = input("Enter starting values: ")
try:
               registers = int(inputString,2)
          except:
               print("Invalid starting values")
               return

          # Check that the input is 4 bits or less
          if registers > 15:
              print("Starting values must be 4 bits or less")
              return

          # Convert the input to a bit array of length 4
          registers = numpy.unpackbits(numpy.uint8(registers), bitorder='little')[0:4]


          # TODO: 
          # Read in the file from sys.argv[1] 
          inputData = readFile(sys.argv[1], 'binary')
          # Make sure you are generating the number of values in the key_stream
          # correctly based on the length of the input_data. This may change based on
          # how you read in the file, and how you create the keyStream.

          # Generate a keystream that is the length of our plaintext or ciphertext in bits
          keyStream = makeKeyStream(registers, len(inputData))

          # Generate the ciphertext or plaintext by XORing the bits with the keyStream bits
          outputData = XOR(inputData, keyStream)

          # Write the file to sys.argv[2] 
          writeFile(sys.argv[2], outputData, 'binary')
          print(f"output written to {sys.argv[2]}")



     elif(action ==2):
          # check for three sys.arg[x]
          if(len(sys.argv) < 4):
               print("Not enough arguments")
               print("Usage: python3 part01_02.py knownPlainTextFile cipherTextFile outputFile")
               return

          # TODO:
          # Read in the knownPlainTextData (sys.argv[1]) and the cipherTextData(sys.argv[2])
          knownPlainText = readFile(sys.argv[1], 'ascii')
          cipherTextData = readFile(sys.argv[2], 'binary')
          # Generate a possible keyStream by XORing the knownPlainText bits with the ciphertextBits
          # Remember you need to account for fewer bits in the knownPlainText in your XOR function
          potentialKeyStream = XOR(knownPlainText, cipherTextData)
# Write file containing possible key_stream
          #write_file(sys.argv[3], binary_string)
          writeFile(sys.argv[3], potentialKeyStream, 'binary')
          print(f"Possible keystream written to {sys.argv[3]}")
          # You will need to determine which bits are XORed together in the function
          # using a Googlesheet or Excel spreadsheet as shown in the lab. For the lab there are only 2 taps being used.
          # Once you have the seed value, return to this program and run the encrypt/decrypt 
          # portion of the program using the discovered seed value and changing the taps in the cycle() function.

     else:
          print("Something went wrong.")

if __name__=="__main__":
     main()
