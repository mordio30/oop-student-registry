class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = None
        self._age = None
        self._grade = None

        self.name = name  # Use the setter for validation
        self.age = age    # Use the setter for validation
        self.grade = grade  # Use the setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.istitle() and new_name.isalpha() and len(new_name) >= 3:
            self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        valid_grades = {"9th", "10th", "11th", "12th"}
        if isinstance(new_grade, str) and new_grade in valid_grades:
            self._grade = new_grade

    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def advance(self, years_advanced=1):
        next_grade = f"{int(self.grade[:-2]) + years_advanced}th" if self.grade[:-2].isdigit() else None
        if next_grade:
            self.grade = next_grade
        return f"{self.name} has advanced to the {self.grade}"

    def study(self, subject):
        return f"{self.name} is studying {subject}"
