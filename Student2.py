
from Object_functions import Student

student1 = Student("Oscar", "Business", 3.1)
student2 = Student("Monika", "Art", 3.8)

# vypíše True nebo False. Podle gpa hodnoty
print(student1.on_honor_roll())
print(student2.on_honor_roll())
