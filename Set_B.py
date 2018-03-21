'''
For a given natural number, determine its palindrome.
'''

def readNumber():
    '''
    Reads a natural number from the keyboard.
    INPUT: None
    OUTPUT: number - the inputed number
    '''
    try:
        number = int(input('Number: '))
        return number
    except ValueError as valueError:
        print(valueError)
        
def getPalindrome(number):
    '''
    Returns the palindrome of a natural number.
    INPUT: number - a natural number
    OUTPUT: palindrome - the palindrome of the number
    '''
    try:
        if number < 0:
            print('unsupported input value for number: must be positive')
            return
        if number < 10:
            palindrome = number
            return palindrome
        palindrome = 0
        while number != 0:
            lastDigit = number % 10
            palindrome = palindrome * 10 + lastDigit
            number = number // 10
        return palindrome
    except TypeError as typeError:
        print(typeError)

def printData(data):
    '''
    Prints the data on the console (it it exists).
    INPUT: data - the data to be printed
    OUTPUT: None
    '''
    if 'None' in str(data):
        return
    print(data)