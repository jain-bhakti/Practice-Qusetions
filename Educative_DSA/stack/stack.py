class Stack:
    def __init__(self):            #constructor function to create satck object
        self.items = []

    def push(self,item):                    #to insert element to stack(named as items)
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return(self.items == [])
 
    def peek(self):
        if not self.is_empty():
            return(self.items[-1])

    def get_stack(self):
        print(self.items)

S = Stack()
S.push("A")
S.push("B")
S.push("C")
S.push("D")
S.get_stack()
S.pop()
if not S.is_empty():
    print("Stack has elements")
else:
    print("Stack is empty")
print(f"The topmost element is {S.peek()}")
S.get_stack()