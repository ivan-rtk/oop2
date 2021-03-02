class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def student_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <=10:
            if course in lecturer.gradesLecturer:
                lecturer.gradesLecturer[course] += [grade]
            else:
                lecturer.gradesLecturer[course] = [grade]
        else:
            print("ошибка student_grade ", lecturer.name, course, grade)
            return 'ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.gradesLecturer = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <=10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("ошибка", student.name, course, grade)
            return 'Ошибка'



student1 = Student('pit', 'ivanov', 'male')
student2 = Student('lisa', 'ivanova', 'female')
lecturer1 = Lecturer('vasya', 'pupkin')
lecturer2 = Lecturer('sasha', 'pupkina')
reviewer1 = Reviewer('aleg', 'ivanov')
reviewer2 = Reviewer('olga', 'ivanova')
student1.courses_in_progress += ['c++', 'go']
student2.courses_in_progress += ['java', 'ios']
lecturer1.courses_attached += ['c++', 'go']
lecturer2.courses_attached += ['java', 'ios']
reviewer1.courses_attached += ['c++', 'go']
reviewer2.courses_attached += ['java', 'ios']
#test = Lecturer('imfghdk', 'tyr')
#test.courses_attached += ['Python', 'java']
student1.student_grade(lecturer1, 'c++', 10)
student1.student_grade(lecturer1, 'go', 10)
reviewer1.rate_hw(student1, 'go', 10)
reviewer2.rate_hw(student2, 'ios', 10)
#print(test.name, test.surname, test.courses_attached)
print(student1.name, student1.surname, student1.courses_in_progress)
print(student1.name, student1.grades)
print(lecturer1.name, lecturer1.gradesLecturer)
