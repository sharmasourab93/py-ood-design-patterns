class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def render(self, x, y):
        print(f"{self.name} tree in {self.color} at ({x}, {y})")


class TreeFactory:
    def __init__(self):
        self._types = {}

    def get_tree_type(self, name, color):
        key = (name, color)
        if key not in self._types:
            self._types[key] = TreeType(name, color)
        return self._types[key]


class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def render(self):
        self.tree_type.render(self.x, self.y)


if __name__ == "__main__":
    factory = TreeFactory()
    trees = [
        Tree(1, 2, factory.get_tree_type("Oak", "Green")),
        Tree(3, 4, factory.get_tree_type("Oak", "Green")),
        Tree(5, 6, factory.get_tree_type("Pine", "Dark Green")),
    ]

    for tree in trees:
        tree.render()
