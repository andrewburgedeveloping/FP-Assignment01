'''
Generate the largest perfect number smaller than a given natural number.
If such a number does not exist, a message should be displayed.
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
        
def getDivisors(number):
    '''
    Returns a list containing the divisors of the input number (except the number itself).
    INPUT: number - a natural number
    OUTPUT: divisors - the list of divisors for the input number
    '''
    divisors = [1]
    for i in range(2, number//2+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def isPerfect(number):
    '''
    Verifies whether the input number is perfect.
    INPUT: number - a natural number
    OUTPUT: True, if the number is perfect, False otherwise
    RAISES: ValueError if the input number is negative
    '''
    if number < 0:
        raise ValueError('unsupported input value for number: must be positive')
    if number == 1:
        return False
    try:
        return number == sum(getDivisors(number))
    except TypeError as typeError:
        print(typeError)
    except ValueError as valueError:
        print(valueError)
   
def getLargestPerfectSmallerThan(number):
    '''
    Returns the largest perfect number smaller than the given number.
    INPUT: number - a natural number
    OUTPUT: largestPerfect - the largest perfect number smaller than the given number
    '''
    try:
        if number >= 0 and number <= 6:
            print('There is no perfect number smaller than ' + str(number) + '.')
            return
        largestPerfect = number - 1
        if isPerfect(largestPerfect):
            return largestPerfect
        while not isPerfect(largestPerfect):
            largestPerfect = largestPerfect - 1
        return largestPerfect
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