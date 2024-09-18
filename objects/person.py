from abc import ABC, abstractclassmethod

class BasePerson(ABC):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.name = fname + ' ' + lname 

    @abstractclassmethod
    def __str__(self):
        pass

class Teacher(BasePerson):
    def __str__(self):
        return 'Mr ' + self.fname + ' ' + self.lname
    
class Student(BasePerson):
    def __str__(self):
        return self.fname + ' ' + self.lname
