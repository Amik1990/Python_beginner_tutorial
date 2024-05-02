# Vytvoříme datový typ (Class) Student a ten použijeme v dokumentu Student.py. Třída Student nám definuje objekt, který si vytvoříme jako "student"
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
