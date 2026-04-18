class MessageSender:
    def send_message(self, subject, body):
        raise NotImplementedError


class EmailSender(MessageSender):
    def send_message(self, subject, body):
        print(f"Email -> {subject}: {body}")


class SlackSender(MessageSender):
    def send_message(self, subject, body):
        print(f"Slack -> {subject}: {body}")


class Alert:
    def __init__(self, message, sender: MessageSender):
        self._message = message
        self._sender = sender

    def send(self):
        self._sender.send_message("Alert", self._message)


if __name__ == "__main__":
    Alert("Server CPU high", EmailSender()).send()
    Alert("Build failed", SlackSender()).send()
