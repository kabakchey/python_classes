class A:

    def __init__(self, name):
        super().__init__()
        print("A.__init__")
        self.attr1 = "attrA"
        self.name = name

    def methodA(self):
        print("methodA")

class B(A):

    def __init__(self, name):
        # A.__init__(self, name)
        super().__init__(name)
        self.attr2="attrB"
        print("B.__init__")

    def methodB(self):
        print("methodB")


class C(A):
    def __init__(self, name):
        # A.__init__(self, name)
        super().__init__(name)
        self.attr2="attrC"
        print("C.__init__")

class D(B, C):
    def __init__(self):
        # B.__init__(self, "nameB")
        # C.__init__(self, "nameC")
        super().__init__("nameC")

        print("D.__init__")

# b = B("AAA")
# print(b.attr1)
# print(b.name)
# b.methodA()
# b.methodB()
#
# c = C()
# print(c.attr1)
# c.methodA()

d = D()

# print(d.attr1)
# d.methodA()
# d.methodB()

