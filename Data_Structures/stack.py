from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)
    
    def peek(self):
        print(self.container[-1])

    def pop(self):
        self.container.pop()

    def is_empty(self):
        if len(self.container) == 0:
            print("Stack is empty")

    def get_size(self):
        print(len(self.container))

    def print(self):
        print(self.container)

s1 = Stack()
s1.push("mango")
s1.push("orange")
s1.push("banana")
s1.push("kiwi")
s1.push("apple")
s1.peek()
s1.get_size()
s1.pop()
s1.print()
