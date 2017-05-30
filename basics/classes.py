
#------------------------------------------------
# class type, id
class Student:
    pass

student = Student()
student2 = Student()

print(id(student))
print(id(student2))


#------------------------------------------------
# class vars and default values
class Student:
    name = ""
    age = 18
    year = 1
    papers = []
    achievements = None # if there is nothing reaasonable


st1 = Student()
st1.year = 2
st1.papers.append("Python course work")

st2 = Student()
st2.name = "Bob"
st2.year = 4
st2.papers.append("ML course work")

print(st1.name, st1.year, st1.age)
print(st2.name, st2.year, st2.age)

#------------------------------------------------
# class vars and default values
class Student:
    name = ""
    age = 18
    year = 1
    papers = []
    major = None # str or dict? if there is nothing reaasonable


st1 = Student()
st1.name = "Alice"
st1.year = 2
st1.papers.append("Python course work")

st2 = Student()
st2.name = "Bob"
st2.year = 4
st2.papers.append("ML course work")

### add another student

print(st1.name, st1.year, st1.age)
print(st2.name, st2.year, st2.age)

#------------------------------------------------
# add logic (1st step: static method)
def print_student_info(student):
    print("Name: ", student.name)
    print("Year: ", student.year)
    print("Age: ", student.age)

print_student_info(st1)
print_student_info(st2)

class Student:
    name = ""
    age = 18
    year = 1
    papers = []
    achievements = None # if there is nothing reaasonable

    @staticmethod
    def print_info(student):
        print("Name: ", student.name)
        print("Year: ", student.year)
        print("Age: ", student.age)

Student.print_info(st1)
Student.print_info(st2)

# but if we look at standard library classes we will see that
# they are called differently:
s1 = "abc"
s1.upper()
# instead of
str.upper(s1)

#------------------------------------------------
# add logic (2st step: non static method)
# we need somehow tell our function about instance
class Student:
    name = ""
    age = 18
    year = 1
    papers = []
    achievements = None # if there is nothing reaasonable

    #! but we don't specify it explicitly
    def print_info(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Age: ", self.age)

    ### add another method
    def assign_major(self):
        pass
    def add_paper(self):
        pass

    ### modify print, check above methods work

#------------------------------------------------
# Initializer
# We might want to create new instances with init values similar as lib types do:
# l = list([1,2,3])
class Student:

    def __init__(self, name, age=18, year=1):
        self.name = name
        self.age = age
        self.year = year
        self.papers = []
        self.achievements = None

    def print_info(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Age: ", self.age)

st1 = Student("Alice")
st2 = Student("Bob", 42, 2)


st1.print_info()
st2.print_info()

### move student to another module
### accompilsh class Course
### accompilsh class Professor
### move into diff. modules
### add student support
### add new attributes (email, loan, is_assigned, head_of_faculty, head_of_commitee, etc)

class Course:

    def __init__(self, name):
        self.name = name
        self.lecturers = []

    def add_lecturer(self, lecturer):
        pass

    def print_info(self):
        pass


class Professor:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        pass

    def print_info(self):
        pass

    
########################################################
# instance vs class difference

class A:
    class_var1 = "abc"
    class_var2 = 42

    def __init__(self, obj_var1, obj_var2):
        self.obj_var1 = obj_var1
        self.obj_var2 = obj_var2

a1 = A("xyz", 123)
a2 = A("efg", 456)

print(a1.class_var1)
print(a1.obj_var1, a1.obj_var2)

print(a2.class_var1)
print(a2.obj_var1, a2.obj_var2)

print(id(a1.class_var1), id(a2.class_var1))
print(id(a2.obj_var1), id(a2.obj_var2))

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
