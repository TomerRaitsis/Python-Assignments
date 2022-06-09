from functools import reduce

class course:
    """
    A class that represents a course, have a name and a grade.

    This class contains a name and a grade, the grade can be changed (using a method)
    """
    def __init__(self,course_name):
        """
        The classes Ctor

        Gets a name as its parameter and sets it as the course name, sets the grade to a default value (101)
        :param course_name: The name of the course
        """
        self.Cname = course_name
        self.grade = 101

    def setGrade(self,newgrade):
        """
        A method for changing the grade (only to a valid grade)

        Gets a grade as its parameter and checks if it is valid, if it is, it will change the grade to the given parameter
        :param newgrade: The new grade given, has to be between 0-100
        :return: There is no return value
        """
        if newgrade > 0 and newgrade < 101:
            self.grade = newgrade

    def __repr__(self):
        """
        This method returns the object representation in string format.

        :return: returns the object representation in string format
        """
        return f'course({self.Cname})'

    def __str__(self):
        """
        This method returns the string representation of the object.

        :return: returns the string representation of the object
        """
        return f'{self.Cname} = {self.grade}'




class student:
    """
    A class that represents a student, has a name and an id (private attribute), also has an array of course objects

    This class contains a name and id (of the student) and an array of his courses.
    courses can be added, the grade needs to be valid. if a course that is about to be added already exists the last
    valid adding will be set.
    """
    def __init__(self,student_name, student_id):
        """
        The classes Ctor

        Gets a name and an id, checks if they are valid and sets them to the name and id attributes.
        Sets the students courses array to an empty list.
        :param student_name: The name of the students(can be letters only)
        :param student_id: The id of the student (can be numbers only)
        """
        if not student_name.isnumeric():
            self.name = student_name
        else:
            raise ValueError()
        if student_id.isnumeric():
            self.__id = student_id
        else:
            raise ValueError()
        self.Scourse = []

    def getID(self):
        """
        A method to get the students id.

        The id is a private attribute, so it will be accessed (to see only) with this method
        :return: Returns the students id
        """
        return self.__id

    def addCourse(self,C):
        """
        A method to add a course the students array

        Gets a course object, if the grade of it is valid there are to options:
        1. If the course does not exists, it will be added to the courses array
        2. If the course exists, the grade of it will change to the grade of the parameter
        :param C: A course object
        :return: There is no return value
        """
        if C.grade >= 0 and C.grade <= 100:
            for c in self.Scourse:
                if c.Cname == C.Cname:
                    c.setGrade(C.grade)
                    return
                else:
                    pass
            self.Scourse.append(C)

    def __str__(self):
        """
        This method returns the string representation of the object.

        :return: returns the string representation of the object
        """
        return f'{self.__id}\n{self.name}\n{self.Scourse}\n'

    def __repr__(self):
        """
        This method returns the object representation in string format.

        :return: returns the object representation in string format
        """
        return f'student({self.name},{self.__id})'


FileName = input('Please enter the name of your file here (.txt will be added automatically): ')
FileName = FileName + '.txt'
try:  # checks if the file exists, prints an error message and ends the program
    with open(FileName, 'r') as f:
        S = []
        lines = f.readlines()
        for line in lines:
            newline = line.strip().split('\t')  # separates to 3 parts: name,id,all courses
            temp_student = student(newline[0], newline[1])
            newline = newline[2].strip().split(';')  # separates the courses
            for pair in range(len(newline)):
                v = newline[pair].split('#')  # separates a course to a name and grade
                temp_course = course(v[0])
                temp_course.setGrade(int(v[1]))
                temp_student.addCourse(temp_course)  # course added to the student
            S.append(temp_student)  # student added to the students array
except FileNotFoundError:
    print('File does not exists\n')
    exit(0)

choice = -1
while choice != 4:
    try:  # checks if the given input is a number, prints an error message if it isn't. user asked again for an input
        choice = int(input('Please choose an option:\n1.Avarage of student\n2.Avarage of course\n3.Avarage of all students\n4.EXIT\nYour Choice: '))
    except ValueError:
        print('Only numbers can be entered!!')
        choice = -1

    if choice == 1:  # calculates the average of a specific student (if exists)
        s_name = input('Please enter name of a student: ')
        chosen_student = list(filter(lambda x: True if x.name == s_name else False,S))  # looks for the student
        if len(chosen_student) > 0:  # in case student exists
            # in the next lines the average is calculated
            grades = list(map(lambda x: x.grade, chosen_student[0].Scourse))
            if len(grades) > 0:
                print(chosen_student[0].getID())
                print(reduce(lambda a,b: a+b,grades)/len(chosen_student[0].Scourse))
            else:
                print('Student has zero courses')
        else:  # in case student does not exists
            print('Student does not exists\n')
    elif choice == 2:  # calculates the average of a specific course (if exists)
        c_name = input('Please enter name of a course: ')
        # in the next line all the courses are filtered to the ones that are as the given parameter
        chosen_course = list(filter(lambda x: True if c_name == x.Cname else False,(reduce(lambda a,b: a + b,map(lambda x: x.Scourse,S)))))
        if len(chosen_course) > 0: # in case course exists
            print(c_name)
            # in the next print the average is calculated
            print(int(reduce(lambda a,b: a + b,map(lambda a: a.grade , chosen_course)))/len(chosen_course))
        else: # in case course does not exists
            print('Course does not exists\n')
    elif choice == 3:  # Writes to a file all the ids of the students and next to each id the students average
        if len(S) > 0:  # checks if there students in the array
            filename = input('Please enter a file name (.txt will be added automatically): ')
            filename = filename + '.txt'
            with open(filename, 'w') as f:
                ids = list(map(lambda x: x.getID(), S))  # an array of ids
                # in the next print all the average are calculated
                courses = list(filter(lambda x: True if len(x) > 0 else False,map(lambda x: list(map(lambda a: a.grade,x)),map(lambda x: x.Scourse, S))))
                avarages = list(map(lambda x: reduce(lambda a,b: a+b,x)/len(x),courses))
                f.write(reduce(lambda a, b: a + b, map(lambda x, y: f'{x} {y}\n', ids, avarages)))  # adding lines to a text
        else:
            print('There are no students!')
    elif choice == 4:
        print('You chose to exit, Good Bye!')
    else:
        print('Please choose a valid option')
