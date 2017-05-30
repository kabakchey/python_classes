import person

class Professor(person.Person):
    def __init__(self, name):
        person.Person.__init__(self, name)
        # self.name = name
        self.courses = []

    def __str__(self):
        str_repr = "Professor name: %s" % self.name
        return str_repr

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def _print_rows(self, lang):
        # print("Professor name: %s" % self.name)

        person.Person._print_rows(self, lang)
        print("Courses:")
        for course in self.courses:
            print(("\t"+ person.Person.FORMAT_VALUE) % course.name)
