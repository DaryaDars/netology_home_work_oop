class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def add_corsess(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average_grades_student(students, course):
        for student in students:
            result = float(sum(student.grades.get(course)) / len(student.grades.get(course)))
            student.average_grades = result
        return

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grades}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.calc_average_grades_student == other.calc_average_grades_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.calc_average_grades_student() < other.calc_average_grades_student()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.calc_average_grades_student() == other.calc_average_grades_student()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_list = []  # возможно убрать это ?

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        # self.average_grades = float()
        # self.lecturers.append(self)  # возможно убрать это ?
        Lecturer.lecturer_list.append(self)

    def calc_average_grades_lecture(lecturers, course):
        for lecturer in lecturers:
            result = float(sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course)))
            lecturer.average_grades = result
        return

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grades}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.average_grades < other.average_grades

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.average_grades > other.average_grades

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.calc_average_grades_lecture == other.calc_average_grades_lecture

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

def courses_average_students(student_list, course):
    for student in student_list:
        for cours_name, average in student.grades_student.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Студент: {student.name} {student.surname}\n"
                        f"Курс: {cours_name}\n"
                        f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")

def courses_average_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for cours_name, average in lecturer.grades_lecturer.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\n"
                        f"Курс: {cours_name}\n"
                        f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")

    # 1 Задание (проверка)
print('==Задание 1==')
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

# # # 2 Задание (проверка)
print('\n\n==Задание 2==')
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}
#
# print(lecturer.average_grades)


    # 3-4 Задание (проверка)
print('\n\n==Задание 3-4 ПОЛЕВЫЕ ИСПЫТАНИЯ==\n')
#Создаем экземпляры класса Student
student1 = Student('Сергей', 'Петров', 'Мужчина')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Дарья', 'Иванова', 'Женщина')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Основы программирования']

#Создаем экземпляры класса Lecturer
lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Петр', 'Миронов')
lecturer2.courses_attached += ['Python', 'Java']

#Создаем экземпляры класса Reviewer
reviewer1 = Reviewer('Инокентий', 'Кот')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Игорь', 'Миронов')
reviewer2.courses_attached += ['Git', 'Java']

#Добавляем оценки студентам за курс Python
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

#Добавляем оценки студентам за курс Git, Java
reviewer2.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student1, 'Java', 9)
reviewer2.rate_hw(student2, 'Java', 10)

#Добавляем оценки лекторам за курс Python
student1.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer2, 'Python', 4)
student2.rate_lecture(lecturer2, 'Python', 9)
#Добавляем оценки лекторам за курс Git, Java
student1.rate_lecture(lecturer1, 'Git', 10)
student2.rate_lecture(lecturer1, 'Git', 7)
student1.rate_lecture(lecturer2, 'Java', 4)
student2.rate_lecture(lecturer2, 'Java', 9)

# #Рассчитываем средние оценки для сутеднтов за курс Python
Student.calc_average_grades_student([student1, student2], 'Python')
#
#Рассчитываем средние оценки для лекторов за курс Python
Lecturer.calc_average_grades_lecture([lecturer1,lecturer2], 'Python')

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

#Проверяем переопределенные методы для созданных классов
print(reviewer1, end='\n\n')
print(lecturer1, end='\n\n')
print(lecturer2, end='\n\n')
print(f'Средняя Оценка lecturer1 > lecturer2: {lecturer1 > lecturer2}')
print(f'Средняя Оценка lecturer1 < lecturer2: {lecturer1 < lecturer2}')
print(f'Средняя Оценка lecturer1 == lecturer2: {lecturer1 == lecturer2}')
print(f'Средняя Оценка student1 > student2: {student1 > student2}')
print(student1, end='\n\n')
print(student2, end='\n\n')