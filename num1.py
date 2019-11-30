# Создайте класс Student, конструктор которого имеет параметры name,lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет: Программирование.”

# class Student:
#     def __init__(self,name,lastname,department,year_of_entrance):
#     self.name = name
#     self.lastname = lastname
#     self.department = department
#     self.year_of_entrance = year_of_entrance
#
# def get_student_info(self):
#     return 'Student: ' + self.name + ' ' + self.surname + ' entered at university ' + str(self.year_of_entrace) + ' ' + ' on the department ' + self.department
#
#
#     student = Student('Frank', 'Iero', 2014, 'Computer Science')
#     print(student.get_student_info())

class Student():
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        name = self.name
        last_name = self.last_name
        department = self.department
        year_of_entrance = self.year_of_entrance
        message = f"{name.title()} {last_name.title()} entered at university  {year_of_entrance} y. on the {department} department."
        return message

go = Student("Frank", "Iero", "Computer Science", "2019")
print(go.get_student_info())


