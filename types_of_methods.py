class Student:

    School = "SHMIT"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #mutator method
    def set_m1(self,m1):
        self.m1 =m1

    #accessor method
    def get_m1(self):
        return self.m1 

    @classmethod
    def schoolInfo(cls):
        return cls.School

    @staticmethod
    def info():
        print("hello this is class of python")

s1 = Student(23,56,86)
s2 = Student(28,87,53)

print(s1.avg())
print(s2.avg())

s1.set_m1(100)
print("New m1",s1.get_m1())
print("New avg",s1.avg())
print(Student.schoolInfo())

Student.info()