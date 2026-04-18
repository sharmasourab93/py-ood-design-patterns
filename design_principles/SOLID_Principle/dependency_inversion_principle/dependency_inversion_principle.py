"""
Dependency Inversion Principle : Flawed
"""


class Manager(object):
    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def add_developer(self, dev):
        self.developers.append(dev)

    def add_designers(self, design):
        self.designers.append(design)

    def add_testers(self, testers):
        self.testers.append(testers)


class Developer(object):
    def __init__(self):
        print("developer added")


class Designer(object):
    def __init__(self):
        print("designer added")


class Testers(object):
    def __init__(self):
        print("tester added")


if __name__ == "__main__":
    a = Manager()
    a.add_developer(Developer())
    a.add_designers(Designer())
