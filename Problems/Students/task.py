class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = f'{self.name[0]}{self.last_name}{self.birth_year}'


f_name = input()
l_name = input()
year = input()
student = Student(f_name, l_name, year)
print(student.id)
