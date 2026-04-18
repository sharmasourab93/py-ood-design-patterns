class Book:
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)


class Food:
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_food(self)


class TaxVisitor:
    def visit_book(self, book: Book):
        return book.price * 1.05

    def visit_food(self, food: Food):
        return food.price * 1.02


if __name__ == "__main__":
    items = [Book(100), Food(50)]
    visitor = TaxVisitor()

    for item in items:
        print(round(item.accept(visitor), 2))

