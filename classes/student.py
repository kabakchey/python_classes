import person

#------------------------------------------------
# class type, id
class Student(person.Person):

    def __init__(self, name, age=18, year=1):
        person.Person.__init__(self, name)
        print("I'm new Student")
        # self.name = name
        self.age  = age
        self.year = year
        self.papers_local = []

    def _print_rows(self, lang):
        person.Person._print_rows(self, lang)
        print(person.Person._format_row("Year", self.year, lang))
        print(person.Person._format_row("Age", self.age, lang))

    def print_papers(self):
        for idx, paper in enumerate(self.papers_local):
            print("Paper %d: %s" %(idx, paper))

