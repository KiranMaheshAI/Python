# Encapsulation

class Student:
    __numberOfStudents = 0  # Class Variables or static Variables
    __schoolName = "MAPS"
    isPlusMember = True

    def __init__(self, name, rollNumber, marks):
        self.rollNumber = rollNumber
        self.name = name
        self.__marks = marks
        self.numberOfStudents = Student.__numberOfStudents+1
        Student.__numberOfStudents += 1

    #getter
    def getMarks(self):
        return self.__marks

    # setter
    def setMarks(self, newMarks):
        self.__marks = newMarks

    @staticmethod
    def getSchoolName():
        return Student.__schoolName
    
    def getStudentSchoolName(self):
        return Student.__schoolName


if __name__ == "__main__":
    s1 = Student("kiran", 123, 45)
    print(s1.getSchoolName())
    print(Student.getSchoolName())
    print(s1.getStudentSchoolName())
    print(s1.getMarks())
    s1.setMarks(90)
    print(s1.getMarks())
