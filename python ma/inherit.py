class school:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def classA(self):
        return self.f_name, self.l_name


class classC(school):
    def __init__(self, f_name, l_name,age):
        super().__init__(f_name, l_name)
        self.age = age

    def Welcome(self):
        super().classA()
        print("Welcome", self.f_name, self.l_name, "hi! how are you?", self.age)


# x = school("Jaya", "Priya")
y = classC("Raj", "kumar",25)
# x.classA()
y.Welcome()
