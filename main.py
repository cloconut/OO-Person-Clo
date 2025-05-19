# Person class (main)
class Person():
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    #M Methods
    def printname(self):
        print(f'First name: {self.first}')
        print(f'Last name: {self.last}')

# Child classes
class Student(Person):
    def __init__(self, first, last, stID, home, mother, father):
        super().__init__(first, last)
        self.studentid = 0
        self.homeroom = home
        self.mother = mother
        self.father = father

    # Methods
    def enrolclass(self):
        return

studentlist = ['clodagh', 'isabelle', 'tanya']
clodagh = Student('Clodagh', 'Campbell', '39366037', 'Barker', 'Sharyn', 'Martin')

# Parent class
class Parent(Person):
    def __init__(self, first, last, occ, alum, gradyear):
        super().__init__(first, last)
        self.occupation = occ
        self.alumni = alum
        self.gradyear = gradyear

    # Methods
    def parentdetails():
        print(f'Parent of {studnet}:')
        print(f'Name: {self.first} {self.last}')
        print(f'Occupation: {self.occ}')
        if alum == 'no':
            print('Not an allumni of Macarthur Anglican School')
        if alum == 'yes':
            print(f'Allumni of Macarthur Anglican School - Class of {self.gradyear}')

sharyn = Parent('Sharyn', 'Robins', 'Conveyancer', 'no', 'n/a')
martin = Parent('Martin', 'Campbell', 'Engineer', 'no', 'n/a')

# Subject class
class Subject():
    def __init__(self, stID, subname):
        super().__init__(stID)
        self.subjectname = subname

    # Methods
    def printstudents(self):
        return

def main():
    studnet = input('Enter Student: ').lower()
    if studnet not in studentlist:
        print('Student not enrolled')
    if studnet in studentlist:
        print('Would you like to:')
        print('1. View Classes')
        print('2. View Parents')
        print('3. something else')
        extra = input('Enter (1/2/3): ')
        if extra == '1':
            return

main()