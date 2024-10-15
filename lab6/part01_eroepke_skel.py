# Lab 06 part 01
# You will be creating a Baby
# Fiestel cipher.  It will have a 4 bit key
# and work with only 4 bits of data. It will run for 3 
# rounds.  You will not be implementing a block
# cipher mode.
#
# The s-box lookup table is provided for you as a numpy array.
#
#
import numpy as np
from typing import Tuple

# S-box lookup table
# Do not modify this table.  It has been provided for you.
def sBox(key: str, index: str) -> int:
    key = int(key, 2)
    index = int(index, 2)
    sBox = np.array([
        [0, 2, 2, 3],
        [2, 3, 0, 0],
        [1, 2, 0, 0],
        [3, 0, 1, 3],
        [2, 0, 3, 1],
        [1, 3, 2, 2],
        [3, 1, 3, 2],
        [0, 1, 2, 1],
        [3, 1, 0, 2],
        [1, 0, 1, 3],
        [0, 3, 3, 0],
        [1, 2, 3, 1],
        [2, 3, 1, 2],
        [3, 1, 0, 0],
        [0, 0, 2, 1],
        [2, 2, 1, 3]
    ])
    return sBox[key, index]

# Encoding for one round of a Fiestel network/cipher
def encodeRoundFunction(inputBits: str, keyBits: str) -> str:
    leftHalf = inputBits[:2]
    rightHalf = inputBits[2:]

    # use the sBox function based upon the right 2 bits in the block and the keyBits

    s = str(sBox(keyBits, rightHalf))

    # TODO:  
    #  1. Assign the new left half the bits in the old right half
    #  2. XOR the old left half bits with the output bits from the sBox to make the new right half
    #  3. join the new left half with the new right half
    
    #Assign new left half i nthe old right half
    leftHalf = rightHalf
    #XOR old left half with sBox output bits and make that the new right half
    rightHalf = format(int(leftHalf, 2) ^ int(s, 10), '02b')

    inputBits = leftHalf + rightHalf

    return inputBits

 
# Shifts the key elements left 
def encodeRotateKey(keyBits: str) -> str:
    keyArray = np.array(list(keyBits))
    # np.roll is a numpy function that shifts elements.
    # A positive number shifts the array elements to the right.  
    # A negative number shifts the array elements to the left. 

    # TODO:  The first bit becomes the last bit in the 4-bit array using np.roll function
    # to shift the array elements to the left and insert the value formerly at index 0 to index 3.
    #Shift the array to the left

    #Shift array to the left by -1
    rotatedKey = np.roll(keyArray, -1)

    return "".join(rotatedKey)

# Encrypt function
def encode(inputBits: str, keyBits: str) -> Tuple[str, str]:
    # TODO:  Loop through the encodeRoundFunction() and encodeRotateKey() three times.
    # Print the values for the final screenshot as a sanity check

    #Loop through the encodedRoundFunction()and ecodeRotateKey() 3 times
    for round in range(3):
        inputBits = encodeRoundFunction(inputBits, keyBits)
        keyBits = encodeRotateKey(keyBits)
        print(f"Round: {round}    {keyBits}")

    return inputBits, keyBits


# Main function  
def main():
    inputBits = input("4-bit input to encode: ")
    keyBits = input("4-bit key: ")
    encode(inputBits, keyBits)


if __name__ == '__main__':
    main()