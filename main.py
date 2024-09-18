from objects.person import Teacher, Student, BasePerson
from objects.school import ClassRoom, School


alireza_kalaie = Teacher('Alireza', 'Kalaie')

class_1_students = [ 
    Student('hamid', 'goli'),
    Student('naser', 'hemati'),
    Student('pejman', 'jamshidi'),
    Student('naser', 'abdollahi')
]

class_room_1 = ClassRoom(name='kharazi' ,students=class_1_students, teacher=alireza_kalaie, code=1)

hesam_doosti = Teacher('Hesam', 'Doosti')
class_2_students = [
    Student('hamid', 'goli'),
    Student('naser', 'hemati'),
    Student('pejman', 'jamshidi'),
    Student('naser', 'abdollahi')
]

class_room_2 = ClassRoom(name='mofateh', students=class_2_students, teacher=hesam_doosti, code=2)

salam_1 = School('salam_1', class_rooms=[class_room_1, class_room_2])


