# Parent class
class Person():
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def printname(self):
        print(first)
        print(last)


# Child classes
class Student(Person):
    def __init__(self, first, last, stID, home):
        super(). __init__(first, last)
        self.studentid = 0
        self.homeroom = home

    # Methods
    def enrolclass(self):

class Parent(Person):
    def __init(self, first, last, occ, alum):
        super().__init__(first, last)
        self.occupation = occ
        self.alumni = alum

class Subject():
    def __init__(stID, subname):
        self.studentid = stID
        self.subjectname = subname

    # Methods
    def printstudents(self):

