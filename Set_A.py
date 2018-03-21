'''
Generate the first prime number larger than a given natural number.
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

def isPrime(number):
    '''
    Verifies whether the input number is prime.
    INPUT: number - a natural number
    OUTPUT: True, if number is prime, False otherwise
    RAISES: ValueError if the number is negative
    '''
    if number < 0:
        raise ValueError('unsupported input value for number: must be positive')
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True

def getFirstPrimeLargerThan(number):
    '''
    Returns the first prime number larger than the given number.
    INPUT: number - a natural number
    OUTPUT: firstPrime - the first prime number larger than the given number
    '''
    try:
        firstPrime = number + 1
        if isPrime(firstPrime):
            return firstPrime
        while not isPrime(firstPrime):
            firstPrime = firstPrime + 1
        return firstPrime
    except TypeError as typeError:
        print(typeError)
    except ValueError as valueError:
        print(valueError)

def printData(data):
    '''
    Prints the data on the console (it it exists).
    INPUT: data - the data to be printed
    OUTPUT: None
    '''
    if 'None' in str(data):
        return
    print(data)