#Part 03

#This program will provide cryptanalysis on a Shift by N cipher using an exhaustive key search
#You can either hard code the ciphertext into the program (easy) or you can prompt for 
#a text file or character input from the command line.
#You will need a function called analyze that will read in the ciphertext and then conduct an 
#exhaustive key search that outputs its key (the N) and the answer in each trial)
#
#Example output:

#Testing shift by:  0
#qefpzixppfpsbovzlli

#Testing shift by:  1
#rfgqajyqqgqtcpwammj

#Testing shift by:  2
#sghrbkzrrhrudqxbnnk

#Look back at parts 01 and 02.  They provide clues on how to implement this.  

def main():
    ciphertext = "OMBBWBPMKPWXXI"
    for shift in range(1, 26):
        plaintext = ""
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        print(f"Testing shift by: {shift}: {plaintext}")
        print()

if __name__ == "__main__":
    main()

