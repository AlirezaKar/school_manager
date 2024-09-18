class School:
    def __init__(self, name, class_rooms):
        self.name = name
        self.class_rooms = class_rooms

class ClassRoom:
    def __init__(self, name, students, teacher, code):
        self.name = name
        self.students = students
        self.teacher = teacher
        self.code = code 
