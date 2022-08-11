class Student:
    def setName(self, name):
        self.name = name
    def setgroup_number(self, group_number):
        self.group_number = group_number
    def setAge(self, age):
        self.age = age
    def getName(self):
        print(self.name)
    def getgroup_number(self):
        return (self.group_number)
    def getAge(self):
        print(self.age)
s = Student
s_name = input()
s.setName(s_name)
s_group_number = input()
s.setgroup_number(s_group_number)