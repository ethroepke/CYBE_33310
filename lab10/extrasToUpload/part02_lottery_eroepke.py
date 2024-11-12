  GNU nano 6.2                                                                                                                  part02_lottery_skel.py *                                                                                                                          
# Lab 10 part 02 - ISU Lottery
# ISU Lottory generates two lottery numbers on odd dates of the month.
# This is the code the use to pull the winning numbers for the odd date and 
# the following even date.
#
# You have to figure out the winning numbers for November 12 based upon
# the numbers for November 11 given in the lab instructions.  
# 
#
import random


#Generates a winning lottery number for today and tomorrow
def generateLottery(dateOfGeneration, timeInSeconds):
    # timeInSeconds = [0, 1, ..., 86400]
    # dateOfGeneration = MM/DD/YYYY
    lotteryNumbers = []

    # Add the date and the seconds to get the seed
    random.seed(int(dateOfGeneration.replace("/","")) + timeInSeconds)

    # Generate lottery number for the current day
    randomNumbers = []
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    # Generate lottery number for the next day
    randomNumbers = []
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    #Return an array of two values
    # lotteryNumbers[0] = Today's lottery number
    # lotteryNumbers[1] = Tomorrow's lottery number
    return lotteryNumbers




def main():
    #Date numbers were generated
    dateOfGeneration = "11/11/2024"
    #Nov 11 winning numbers
    lotteryNumberTarget = "8-3-9-5-7-4-4-7-6-7"
    #Place to store values when get time found and solve lottery number
    timeInSecondsFound = None
    winningTicketTomorrow = None

    #loop through all seconds in a day
    for timeInSeconds in range(86400):
        lotteryNumbers = generateLottery(dateOfGeneration, timeInSeconds)
        #check if generated lottery number matches target number.
        #If so then store time found and lottery number
        if lotteryNumbers[0] == lotteryNumberTarget:
            timeInSecondsFound = timeInSeconds
            winningTicketTomorrow = lotteryNumbers[1]
            break

    #print if solved time in seconds
    if timeInSeconds is not None:
        print(f"Time in seconds matched: {timeInSecondsFound}")
        print(f"Winning ticket for November 12, 2024: {winningTicketTomorrow}")
    else:
        print("No matching time in seconds")


if __name__ == '__main__':
    main()

