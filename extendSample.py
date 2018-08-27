# 继承
class SchoolMember:
    '''代表学校里的成员'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('我是学校成员"{}"'.format(self.name))
    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name,self.age))

class Teacher(SchoolMember):
    '''代表一个老师'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('我是老师"{}"'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('我是学生'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t=Teacher('张老师',29,3000)
t.tell()
s=Student('小明',8,100)
s.tell()