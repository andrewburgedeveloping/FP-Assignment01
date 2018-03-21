'''
Program Entry Point
'''

from Set_A import readNumber, printData, getFirstPrimeLargerThan
from Set_B import getPalindrome
from Set_C import getLargestPerfectSmallerThan

def printMenu():
    menu = 'Problems:\n'
    menu += '1. Set A) Generate the first prime number larger than a given natural number.\n'
    menu += '2. Set B) For a given natural number, determine its palindrome.\n'
    menu += '3. Set C) Generate the largest perfect number smaller than a given natural number.\n'
    menu += '0. Exit'
    print(menu)
 
def readCommand():
    '''
    Reads a natural number from the keyboard.
    INPUT: None
    OUTPUT: command - the inputed number
    '''
    try:
        command = int(input('Command: '))
        return command
    except ValueError:
        pass
    
def main():
    '''
    Runs the Application
    '''
    printMenu()
    while True:
        print()
        command = readCommand()
        if command == 1:
            number = readNumber()
            printData('The first prime number larger than ' + str(number) + ' is ' + str(getFirstPrimeLargerThan(number)) + '.')
        elif command == 2:
            number = readNumber()
            printData('The palindrome of ' + str(number) + ' is ' + str(getPalindrome(number)) + '.')
        elif command == 3:
            number = readNumber()
            printData('The largest perfect number smaller than ' + str(number) + ' is ' + str(getLargestPerfectSmallerThan(number)) + '.')
        elif command == 0:
            break
        else:
            print('Unknown command.')
        
main()