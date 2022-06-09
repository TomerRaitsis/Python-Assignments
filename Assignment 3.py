from functools import reduce

class TreeError(Exception):
    """
    A class that inherits from Exception class, to handle the tree errors
    """
    def __init__(self, V):
        """
        A Constructor

        :param V: A value of the object
        """
        self.v = V
    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'Could not erase {self.v}'
    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows ow the object of this class if created
        """
        return f'TreeError({self.v})'

class TreeValueDoesNotExist(TreeError):
    """
    A class that inherits from Exception class, to handle the tree errors
    """
    def __init__(self, V):
        """
        A Constructor

        :param V: A value of the object
        """
        self.v = V
    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.v}  does not exist or is the node'
    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows ow the object of this class if created
        """
        return f'TreeValueDoesNotExist({self.v})'

class TreeIllegalValue(TreeError):
    """
    A class that inherits from Exception class, to handle the tree errors
    """
    def __init__(self, V):
        """
        A Constructor

        :param V: A value of the object
        """
        self.v = V
    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.v} is not a leaf'
    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows ow the object of this class if created
        """
        return f'TreeIllegalValue({self.v})'


class NTree:
    """
    A class that can create a tree with up to 4 sons for each node,
    possible actions: create, add, delete and print.
    """
    def __init__(self,data):
        """
        A Constructor that creates a new node with 2 empty arrays for the sons

        :param data: The value of the node
        """
        self.entry = data
        self.Leftsons = []
        self.Rightsons = []

    def __str__(self):
        """
        An str operator used to print an object of this class

        :return: A string that will be printed
        """
        return f'{self.entry}{str(self.Leftsons + self.Rightsons).replace(",",";")}'

    def __repr__(self):
        """
        A repr operator to know how the object of this class if created

        :return: A string that shows ow the object of this class if created
        """
        return f'NTree({self.entry}{self.Leftsons + self.Rightsons})'

    def __lt__(self,T):
        """
        A method that returns true if the given parameter is bigger than the current object

        :param T: The value to compare
        :return: True or False
        """
        return self.entry < T.entry

    def Add_To_NTree(self, T):
        """
        A method that adds a new value to the tree

        :param T: The new value
        :return: No return value
        """
        if T.entry not in NTree.Add_To_NTree.Arr:
            if T.entry < self.entry and len(self.Leftsons) == 0:
                NTree.Add_To_NTree.Arr.append(T.entry)
                self.Leftsons.append(T)
                self.Leftsons.sort()

            elif T.entry > self.entry and len(self.Rightsons) == 0:
                NTree.Add_To_NTree.Arr.append(T.entry)
                self.Rightsons.append(T)
                self.Rightsons.sort()

            elif T.entry < self.entry and len(self.Leftsons) == 2:
                if T.entry < self.Leftsons[0].entry and T.entry < self.Leftsons[1].entry:
                    self.Leftsons[0].Add_To_NTree(T)
                elif T.entry > self.Leftsons[0].entry and T.entry > self.Leftsons[1].entry:
                    self.Leftsons[1].Add_To_NTree(T)
                elif T.entry > self.Leftsons[0].entry and T.entry < self.Leftsons[1].entry:
                    self.Leftsons[0].Add_To_NTree(T)

            elif T.entry > self.entry and len(self.Rightsons) == 2:
                if T.entry < self.Rightsons[0].entry and T.entry < self.Rightsons[1].entry:
                    self.Rightsons[0].Add_To_NTree(T)
                elif T.entry > self.Rightsons[0].entry and T.entry > self.Rightsons[1].entry:
                    self.Rightsons[1].Add_To_NTree(T)
                elif T.entry > self.Rightsons[0].entry and T.entry < self.Rightsons[1].entry:
                    self.Rightsons[0].Add_To_NTree(T)

            elif T.entry < self.entry and len(self.Leftsons) == 1:
                NTree.Add_To_NTree.Arr.append(T.entry)
                self.Leftsons.append(T)
                self.Leftsons.sort()

            elif T.entry > self.entry and len(self.Rightsons) == 1:
                NTree.Add_To_NTree.Arr.append(T.entry)
                self.Rightsons.append(T)
                self.Rightsons.sort()



    def Remove_From_Tree(self, T):
        """
        A method that removes a value from the tree

        :param T: The value that needs to be erased
        :return: No return value
        """
        if T.entry in NTree.Add_To_NTree.Arr:
            if self.CheckValueLeft(T):
                for i in self.Leftsons:
                    if T.entry == i.entry:
                        if len(i.Leftsons) == 0 and len(i.Rightsons) == 0:
                            if T.entry in NTree.Add_To_NTree.Arr:
                                NTree.Add_To_NTree.Arr.pop(NTree.Add_To_NTree.Arr.index(T.entry))
                            self.Leftsons.remove(i)
                        else:
                            raise TreeIllegalValue(T)
            elif self.CheckValueRight(T):
                for i in self.Rightsons:
                    if T.entry == i.entry:
                        if len(i.Leftsons) == 0 and len(i.Rightsons) == 0:
                            if T.entry in NTree.Add_To_NTree.Arr:
                                NTree.Add_To_NTree.Arr.pop(NTree.Add_To_NTree.Arr.index(T.entry))
                            self.Rightsons.remove(i)
                        else:
                            raise TreeIllegalValue(T)
            else:
                if T.entry < self.entry and T.entry < self.Leftsons[0].entry:
                    self.Leftsons[0].Remove_From_Tree(T)
                elif T.entry < self.entry and T.entry > self.Leftsons[1].entry:
                    self.Leftsons[1].Remove_From_Tree(T)
                elif T.entry < self.entry and T.entry < self.Leftsons[1].entry and T.entry > self.Leftsons[0].entry:
                    self.Leftsons[0].Remove_From_Tree(T)

                if T.entry > self.entry and T.entry < self.Rightsons[0].entry:
                    self.Rightsons[0].Remove_From_Tree(T)
                elif T.entry > self.entry and T.entry > self.Rightsons[1].entry:
                    self.Rightsons[1].Remove_From_Tree(T)
                elif T.entry > self.entry and T.entry < self.Rightsons[1].entry and T.entry > self.Rightsons[0].entry:
                    self.Rightsons[0].Remove_From_Tree(T)
        else:
            raise TreeValueDoesNotExist(T.entry)

        if T.entry in NTree.Add_To_NTree.Arr:
            NTree.Add_To_NTree.Arr.pop(NTree.Add_To_NTree.Arr.index(T.entry))

    def CheckValueLeft(self,T):
        """
        Checks if the value exists in the left sons

        :param T: The value
        :return: True or false
        """
        for i in self.Leftsons:
            if T.entry == i.entry:
                return True
    def CheckValueRight(self, T):
        """
        Checks if the value exists in the right sons

        :param T: The value
        :return: True or false
        """
        for i in self.Rightsons:
            if T.entry == i.entry:
                return True

NTree.Add_To_NTree.Arr = []


#################### Menu
choice = -1
Tree = -1
while int(choice != 5):
    print('Please choose one of the options below:\n1. Create\n2.Add\n3.Delete\n4.Print\n5. EXIT\n')
    try:
        choice = input('Please enter your choice: ')
        if int(choice) == 1:
            NTree.Add_To_NTree.Arr = []
            Tree = NTree(input('Please enter the first value of you tree: '))
        elif int(choice) == 2:
            if Tree != -1:
                Tree.Add_To_NTree(NTree(input('Please enter a value to add for your tree: ')))
            else:
                raise UnboundLocalError
        elif int(choice) == 3:
            if Tree != -1:
                Tree.Remove_From_Tree(NTree(input('Please enter a value to erase from your tree: ')))
            else:
                raise UnboundLocalError
        elif int(choice) == 4:
            if Tree != -1:
                print(Tree)
        elif int(choice) == 5:
            choice = 5
            print("Thank You, Good Bye")
        else:
            print('Wrong input, Please try again\n')
    except UnboundLocalError:
        print('Illegal option, Please try again\n')
    except (TreeError,TreeValueDoesNotExist,TreeIllegalValue) as t:
        print(f'{t}')
        print(Tree)
    except:
        print('Universal Error\n')
        exit(1)



