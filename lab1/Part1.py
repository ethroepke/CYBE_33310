#Part 01:

#This program will prompt the user for a sentence.
#The program passes the sentence to a function named modify().
#The function modify() returns a string that shifts the characters
#in the sentence three characters to the left.


#Modify function:
#  Takes in a list and then
#  iterates through it shifting the
#  characters three to the left 
#  and returns a string.

#Main
def main():
    sentence = input("Write a sentence without spaces: ")
    shift3 = sentence[3:] + sentence[:3]
    print(shift3)

if __name__ == "__main__":
    main()

C