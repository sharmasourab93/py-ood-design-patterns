class ChatMediator:
    def __init__(self):
        self._users = []

    def register(self, user):
        self._users.append(user)

    def broadcast(self, sender, message):
        for user in self._users:
            if user is not sender:
                user.receive(sender.name, message)


class User:
    def __init__(self, name, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        mediator.register(self)

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self._mediator.broadcast(self, message)

    def receive(self, sender_name, message):
        print(f"{self.name} receives from {sender_name}: {message}")


if __name__ == "__main__":
    mediator = ChatMediator()
    alice = User("Alice", mediator)
    bob = User("Bob", mediator)
    charlie = User("Charlie", mediator)

    alice.send("Build is green.")
    bob.send("Deploying to staging.")
