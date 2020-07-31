class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        item = self.stack[len(self.stack) - 1]
        self.stack.remove(self.stack[len(self.stack) - 1])
        return item

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if not self.stack:
            return True
        return False
