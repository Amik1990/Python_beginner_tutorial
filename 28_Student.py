# Z dokumentu "Classes_objects" naimportuju třídu Student

from Classes_objects import Student

student1 = Student("Daniel", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)


# vygeneruje jméno a pak gpa dle formátu třídy Student
print(student1.name)
print(student1.gpa)
print(student2.major)
