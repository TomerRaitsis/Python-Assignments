############### Assigment 1
class Shekel:
    """
    A class that represents a "Shekel" coin
    """
    def __init__(self, V):
        """
        A constructor

        :param V: The value that will be set as the object value
        """
        self.__OriginalValue = float(V)

    def amount(self):
        """
        A method that returns the amount in shekels (same as the original value)

        :return: The amount
        """
        return float(self.__OriginalValue)

    def GetOriginalValue(self):
        """
        A method that returns the original value

        :return: The original value
        """
        return self.__OriginalValue

    def SetOriginalValue(self, v):
        """
        A method that sets a new value to the original value

        :param v: A new value
        :return: No return value
        """
        self.__OriginalValue = v

    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows ow the object of this class if created
        """
        return f'Shekel({self.__OriginalValue})'

    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.__OriginalValue}nis\n'

    def __add__(self,a):
        """
        An add operator that add the current object to the given one

        :param a: The object that will be added
        :return: The sum of the two
        """
        return float(self.amount() + a.amount())

    def __name__(self):
        """
        A name operator used to show the name of the class

        :return: A string that will be printed
        """
        return 'Shekel'


class Dollar:
    """
    A class that represents a "Dollar" coin
    """
    def __init__(self, V):
        """
        A constructor

        :param V: The value that will be set as the object value
        """
        self.__OriginalValue = float(V)

    def amount(self):
        """
        A method that returns the amount in shekels

        :return: The amount
        """
        return float(self.__OriginalValue * rates[('dollar','nis')])

    def GetOriginalValue(self):
        """
        A method that returns the original value

        :return: The original value
        """
        return self.__OriginalValue

    def SetOriginalValue(self, v):
        """
        A method that sets a new value to the original value

        :param v: A new value
        :return: No return value
        """
        self.__OriginalValue = v

    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows how the object of this class if created
        """
        return f'Dollar({self.__OriginalValue})'

    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.__OriginalValue}$\n'

    def __add__(self,a):
        """
        An add operator that add the current object to the given one

        :param a: The object that will be added
        :return: The sum of the two
        """
        return float(self.amount() + a.amount())

    def __name__(self):
        """
        A name operator used to show the name of the class

        :return: A string that will be printed
        """
        return 'Dollar'

class Euro:
    """
    A class that represents a "Euro" coin
    """
    def __init__(self, V):
       """
        A constructor

        :param V: The value that will be set as the object value
        """
       self.__OriginalValue = float(V)

    def amount(self):
        """
        A method that returns the amount in shekels

        :return: The amount
        """
        return float(self.__OriginalValue * rates[('euro','nis')])

    def GetOriginalValue(self):
        """
        A method that returns the original value

        :return: The original value
        """
        return self.__OriginalValue

    def SetOriginalValue(self,v):
        """
        A method that sets a new value to the original value

        :param v: A new value
        :return: No return value
        """
        self.__OriginalValue = v

    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows how the object of this class if created
        """
        return f'Euro({self.__OriginalValue})'

    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.__OriginalValue}€\n'

    def __add__(self,a):
        """
        An add operator that add the current object to the given one

        :param a: The object that will be added
        :return: The sum of the two
        """
        return float(self.amount() + a.amount())

    def __name__(self):
        """
        A name operator used to show the name of the class

        :return: A string that will be printed
        """
        return 'Euro'

def add(a,b):
    """
    Adds two objects

    :param a: Object a
    :param b: Object b
    :return: The result
    """
    return float(a.amount() + b.amount())
def sub(a,b):
    """
    Subs two objects

    :param a: Object a
    :param b: Object b
    :return: The result
    """
    return float(a.amount() - b.amount())

def type_tag(x):
    """
    Returns the name of the given object class name

    :param x: An object
    :return: A string of the objects class name
    """
    return type_tag.tags[type(x)]
type_tag.tags = {Shekel:'nis', Dollar:'dollar', Euro:'euro'}


def add_D_N(a, b):
    """
    Adds a dollar and shekel objects

    :param a: object
    :param b: object
    :return: The result as a Dollar
    """
    return Dollar(add(b, a) / rates[('dollar', 'nis')])
def add_N_D(a, b):
    """
    Adds a shekel and dollar objects

    :param a: object
    :param b: object
    :return: The result as a Shekel
    """
    return Shekel(add(a, b))
def add_D_E(a, b):
    """
    Adds a dollar and euro objects

    :param a: object
    :param b: object
    :return: The result as a Dollar
    """
    return Dollar(add(b, a) / rates[('dollar', 'nis')])
def add_E_D(a, b):
    """
    Adds a euro and a dollar objects

    :param a: object
    :param b: object
    :return: The result as a Euro
    """
    return Euro(add(b, a) / rates[('euro', 'nis')])
def add_E_N(a, b):
    """
    Adds a euro and shekel objects

    :param a: object
    :param b: object
    :return: The result as a Euro
    """
    return Euro(add(b, a) / rates[('euro', 'nis')])
def add_N_E(a, b):
    """
    Adds a shekel and euro objects

    :param a: object
    :param b: object
    :return: The result as a shekel
    """
    return Shekel(add(a, b))


def sub_D_N(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Dollar
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Dollar(add(b, a) / rates[('dollar', 'nis')])
def sub_N_D(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Shekel
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Shekel(add(a, b))
def sub_D_E(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Dollar
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Dollar(add(b, a) / rates[('dollar', 'nis')])
def sub_E_D(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Euro
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Euro(add(b, a) / rates[('euro', 'nis')])
def sub_E_N(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Euro
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Euro(add(b, a) / rates[('euro', 'nis')])
def sub_N_E(a, b):
    """
    Same as Add but Sub

    :param a: object
    :param b: object
    :return: The result as a Shekel
    """
    b.SetOriginalValue(-b.GetOriginalValue())
    return Shekel(add(a, b))

def apply(str,a,b):
    """
    Gets the name of the operation and returns the result of the suitable function with the parameters

    :param str: string of the operation
    :param a: object
    :param b: object
    :return: Result after applying the function on the parameters
    """
    apply.implemantions = {('add',('dollar','nis')):add_D_N, ('add',('euro','nis')):add_E_N
        , ('add',('nis','dollar')):add_N_D , ('add',('dollar','euro')):add_D_E, ('add',('euro','dollar')):add_E_D
        , ('add',('nis','euro')):add_N_E, ('sub',('dollar','nis')):sub_D_N, ('sub',('euro','nis')):sub_E_N
        , ('sub',('nis','dollar')):sub_N_D , ('sub',('dollar','euro')):sub_D_E, ('sub',('euro','dollar')):sub_E_D
        , ('sub',('nis','euro')):sub_N_E}
    return apply.implemantions[(str,(type_tag(a),type_tag(b)))](a,b)


coercions = {('dollar','nis'):lambda x: Shekel(x.amount()) , ('euro','nis'):lambda x: Shekel(x.amount()),
             ('euro','dollar'):lambda x: Shekel(x.amount())}


def coerce_apply(str,a,b):
    """
    Gets the name of the operation and returns the result of the suitable function with the parameters
    by trying to coerce the objects to the same one

    :param str: string of the operation
    :param a: object
    :param b: object
    :return: Result after applying the function on the parameters
    """
    tx, ty = type_tag(a), type_tag(b)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, a = ty, coercions[(tx, ty)](a)
            a = Shekel(a.amount())
            b = Shekel(b.amount())
            tx = 'nis'
        elif (ty, tx) in coercions:
            ty, b = tx, coercions[(ty, tx)](b)
            a = Shekel(a.amount())
            b = Shekel(b.amount())
            tx = 'nis'
        else:
            return 'No coercion possible.'
    key = (str, tx)
    return coerce_apply.implementations[key](a, b)


coerce_apply.implementations = {('add','nis'): lambda x,y: Shekel(add(x,y) ), ('sub','nis'):lambda x,y: Shekel(sub(x,y)) }

##################### ASSIGNMENT 1/a
rates = {('dollar', 'nis'): 3.82, ('euro', 'nis'): 4.07, ('euro', 'dollar'): 1.06}
s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.amount())
print(e.amount())
print(d + s)
print(add(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)

################### ASSIGNMENT 1/b
print(apply('add', Shekel(50), Dollar(20)))
rates[('euro', 'dollar')] = 1.06
print(apply('add', Dollar(50), Euro(20)))
print(apply('sub', Dollar(50), Euro(20)))

################## ASSIGNMENT 1/c
print(coercions[('dollar', 'nis')](Dollar(50)))
print(coerce_apply('add', Shekel(50), Dollar(20)))
print(coerce_apply('add', Dollar(50), Euro(20)))
print(coerce_apply('sub', Dollar(50), Euro(20)))





