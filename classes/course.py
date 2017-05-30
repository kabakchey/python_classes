

class Course:

    def __init__(self, name):
        self.name = name
        self.lecturers = []

    def add_lecturer(self, lecturer):
        if lecturer not in self.lecturers:
            self.lecturers.append(lecturer)

    def print_info(self):
        print("Course title: %s" % self.name)
        print("Lecturers:")
        for lecturer in self.lecturers:
            print("\t%s" % lecturer.name)
