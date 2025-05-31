class client:
    def init(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


c = client(1, "abc")
print(c.get_id())
print(c.get_name())
