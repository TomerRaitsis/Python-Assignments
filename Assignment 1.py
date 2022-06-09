""" Tomer Raitsis, 316160167 """

def factorSum(n):
    """
    Calculates and returns the sum of all n's primary numbers.

    :param n: A number for calculating his primary numbers
    :return: The sum of the primary digits
    """
    nums = set()
    i = 2
    while n != 1:
        if n % i == 0:
            n = n/i
            nums.add(i)
            i=2
        else :
            i+=1
    list1 = list(nums)
    sum = 0
    for i in range(len(nums)):
        sum += list1[i]

    return sum



def onlyPositive(f):
    """
    Returns a new function that applyes the parameter function on a given parameter(number), if the number is negative
    the function will use the number's opposit.

    :param f: A funtion that will be used in the new function
    :return: return the new function
    """
    def newFunc(num):
        if num >= 0:
            return f(num)
        else:
            return f(-1 * num)
    return newFunc



def interceptPoint(t1,t2):
    """
    Calculates and returns the intercept point between 2 points,
    if there isn't an intercept point it will return None

    :param t1: Tupple for Coordinates
    :param t2: Tupple for Coordinates
    :return: Returns the interception point or None
    """
    x,y = 0, 0
    if t1[0] / t2[0] == 1:
        return None
    else:
        x = (t2[1] - t1[1]) / (t1[0] - t2[0])
        y = t1[0] * x + t1[1]
    return (x,y)




def printNumbers(start, end, num):
    """
    A recursive function that prints the numbers from the starting to the end,
    don't prints the number given as a parameter

    :param start: First number
    :param end: Last number
    :param num: The number that will not be printed
    :return: Nothing is returned
    """
    if start != num:
        print(start)
    if start == end:
       return 0
    if start < end:
        return printNumbers(start + 1, end, num)
    else:
        return printNumbers(start - 1, end, num)




def arrProduct(arr1,arr2):
    """
    Returns an array that has the numbers from the first array as the number of times they appear in the same
    index in the second array. The input arays are in the same size

    :param arr1: Array 1
    :param arr2: Array 2
    :return: The new array as requested
    """
    n = len(arr1)
    newArr =[]
    for i in range(n):
        j = 0
        while j < arr2[i]:
            newArr.append(arr1[i])
            j += 1
    return newArr



def analyze(str):
    """
    Counts the months that had more than 75 mm of rain

    :param str: String that has all the data of rain amounts
    :return: The number of months with more than 75 mm of rain
    """
    count = 0
    newArr = list(str.split(","))
    for i in range(len(newArr)):
        if float(newArr[i]) > 75:
            count += 1
    return count
