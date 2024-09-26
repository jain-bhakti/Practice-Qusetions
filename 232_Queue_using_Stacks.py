class MyQueue:

    def __init__(self):
        self.queue = []
        self.result = ["null"]

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.result.append("null")

    def pop(self) -> int:
        self.result.append(self.queue[0])
        self.queue.remove(self.queue[0])


    def peek(self) -> int:
        self.result.append(self.queue[0])
        
    def empty(self) -> bool:
        n = len(self.queue)
        if n == 0:
            self.result.append("True")
            return 
        self.result.append("False")
        

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(2)
obj.pop()
print(obj)
print(obj.peek())
print(obj.empty())
print(obj.result)