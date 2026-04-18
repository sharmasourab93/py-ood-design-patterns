from dataclasses import dataclass


@dataclass(frozen=True)
class EditorMemento:
    content: str


class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento: EditorMemento):
        self.content = memento.content


class History:
    def __init__(self):
        self._states = []

    def push(self, memento: EditorMemento):
        self._states.append(memento)

    def pop(self):
        return self._states.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Draft 1")
    history.push(editor.save())

    editor.write(" + Draft 2")
    print(editor.content)

    editor.restore(history.pop())
    print(editor.content)

