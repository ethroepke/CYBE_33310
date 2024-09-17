#Lab 02 Part01:

#ETHAN ROEPKE

#This program will 
#  read in a ciphertext file (Yes)
#  count the total number of characters (Yes) 
#  count the number of occurrences of each character in the ciphertext (Yes) 
#  calculate the percentages (Yes)
#  store the counts and percentages in a list of lists (Yes) 
#  print out the percentages in descending order (Yes)
#  print out possible solutions until a plaintext solution is found (Yes)
#  You must show all the iterations you have completed in finding the plain text (Yes)

from collections import Counter
import string
#Main
def main():
    #Read the file and print the file
    print("This is the content of the file:")
    with open("cipherText.txt", "r") as file:
        content = file.read()

    print(content)

    #Removes unwanted non-alphabetic characters to clean up
    updateContent = [char.upper() for char in content if char.upper() in string.ascii_uppercase]

    #Place holder for number of letters in file to get percentage
    totalLetters = len(updateContent)
    print(f"Total number of letters: {totalLetters}")
    #Get the word count of each letter and percentage and organize from most frequent letter
    print("")
    print("This is the letter frequncy list:")

    letterFrequency = Counter(updateContent)
    print("Character  Count        Percentage")

    #This is where we sort the letters and print them
    #Add letters with a count of 0(Not sure why but if not include this it wont print letters that include no characters)
    for letter in string.ascii_uppercase:
        if letter not in letterFrequency:
            letterFrequency[letter] = 0
    sortedLetterFrequency = letterFrequency.most_common()
    for letter, count in sortedLetterFrequency:
        #Math to get percentage of each letter
        percentage = (count / totalLetters)* 100
        print(f"{letter}          {count}          {percentage:.2f}%")

    #Mapping to decrypt cipherr text
    print("")
    print("Testing letter frequency:")

    #TEST1  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "o").replace("J", "i").replace("K", "n").replace("X", "s").replace("S", "h").replace("W", "r").replace("U", "d").replace("G", "l").replace("N", "c").replace("V", "u").replace("Y", "m").replace("T", "w").replace("P", "f").replace("H", "g").replace("Z", "y").replace("L", "p").replace("O", "b").replace("F", "v").replace("B", "k").replace("M", "j")
    #Test2  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "s").replace("K", "n").replace("X", "h").replace("S", "o").replace("W", "i").replace("U", "d").replace("G", "l").replace("N", "c").replace("V", "u").replace("Y", "m").replace("T", "w").replace("P", "f").replace("H", "g").replace("Z", "y").replace("L", "p").replace("O", "b").replace("F", "v").replace("B", "k").replace("M", "j")
    #Test3  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "i").replace("X", "s").replace("S", "o").replace("W", "r").replace("U", "d").replace("G", "l").replace("N", "c").replace("V", "u").replace("Y", "m").replace("T", "w").replace("P", "f").replace("H", "g").replace("Z", "y").replace("L", "p").replace("O", "b").replace("F", "v").replace("B", "k").replace("M", "j")
    #Test4  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "c").replace("G", "d").replace("N", "l").replace("V", "m").replace("Y", "w").replace("T", "u").replace("P", "g").replace("H", "f").replace("Z", "y").replace("L", "p").replace("O", "b").replace("F", "v").replace("B", "k").replace("M", "j")
    #Test5  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "l").replace("G", "m").replace("N", "d").replace("V", "c").replace("Y", "g").replace("T", "u").replace("P", "w").replace("H", "f").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "b").replace("M", "j")
    #Test6  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "l").replace("G", "m").replace("N", "d").replace("V", "u").replace("Y", "g").replace("T", "c").replace("P", "w").replace("H", "f").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "b").replace("M", "j")
    #Test7  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "m").replace("G", "l").replace("N", "d").replace("V", "u").replace("Y", "c").replace("T", "g").replace("P", "w").replace("H", "f").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "b").replace("M", "j")
    #Test8  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "f").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "g").replace("P", "d").replace("H", "m").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "b").replace("M", "j")
    #Test9  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "d").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "g").replace("P", "f").replace("H", "m").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "b").replace("M", "j")
    #Test10  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace("W", "r").replace("U", "d").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "b").replace("P", "f").replace("H", "m").replace("Z", "y").replace("L", "p").replace("O", "k").replace("F", "v").replace("B", "g").replace("M", "j")
    #Test11  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace ("W", "r").replace("U", "d").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "b").replace("P", "g").replace("H", "m").replace("Z", "y").replace ("L", "p").replace("O", "k").replace("F", "v").replace("B", "f").replace("M", "j")
    #Test12  decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace ("W", "r").replace("U", "d").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "b").replace("P", "g").replace("H", "m").replace("Z", "y").replace ("L", "p").replace("O", "k").replace("F", "f").replace("B", "v").replace("M", "j")
    #Test13 - this is the final mapping
    decryptTest = content.replace("I", "e").replace("C", "t").replace("R", "a").replace("Q", "h").replace("J", "n").replace("K", "o").replace("X", "s").replace("S", "i").replace ("W", "r").replace("U", "d").replace("G", "l").replace("N", "w").replace("V", "u").replace("Y", "c").replace("T", "b").replace("P", "g").replace("H", "m").replace("Z", "y").replace ("L", "p").replace("O", "f").replace("F", "k").replace("B", "v").replace("M", "j")


    print(decryptTest)

if __name__ == "__main__":
    main()
