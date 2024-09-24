#  conduct a trigram analysis on the ciphertext
#  find the starting indices for each of the most common trigrams
#  calculate the distance between the starting index of each common trigram
#  determine the common factors of the differences to determine the key length
#  break the cipher into X (key length value) number of shift-by-n ciphers
#  perform monoalphabetic frequency analysis for each of the X shift-by-n ciphers
#  identify the potential key 
#  use the key to decrypt the ciphertext into plaintext

#  You must print all the iterations you have completed in finding the plaintext

from collections import Counter
from collections import defaultdict
import string

#Main function
def main():

    #Reads file and prints the contents in file
    print("This is the contents of the file:")
    with open("cipherText.txt", "r") as file:
        content = file.read()
    print(content)

    #Initialize a list to store trigrams and a dictionary to keep track of starting indexes for each trigram
    trigrams = []
    trigramIndexes = defaultdict(list)

    #Loop through content to create trigrams
    for i in range(len(content) - 2):
        trigram = (content[i], content[i+1], content[i+2])
        trigrams.append(trigram)
        trigramIndexes[trigram].append(i)

    #This will keep a counter for trigrams appear throughout file
    trigramCount = Counter(trigrams)

    #Get us the top 10  most common trigrams
    mostTrigrams = trigramCount.most_common(10)

    #Print the trigrams and the count for each
    print("\nMost Common Trigrams:")
    for trigram, count in mostTrigrams:
        startingIndexes = trigramIndexes[trigram]
        print(f"{''.join(trigram)}: {count}\nStarting indexes: {startingIndexes}")
        #Calculate the difference for each trigram at starting index
        indexDifference = [startingIndexes[i + 1] - startingIndexes[i] for i in range(len(startingIndexes) - 1)]
        print(f"Index Differences: {indexDifference}\n")


if __name__=="__main__":
   main()