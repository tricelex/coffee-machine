class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name[0]}{self.last_name}{self.birth_year}"

print(Student(*[input() for _ in range(3)]))
