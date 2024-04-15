#%%
# basic function for stack
class Stack:
    def __init__(self):
        self.list = []
        self.size = 0
    
    
    def push (self, x):
        self.list.append(x)
        self.size += 1
    
    def pop (self):
        if self.size:
            val = self.list.pop()
            self.size -= 1
        return val
    
    def peek(self):
        return self.list[-1]
    
    def getsize (self):
        return self.size
    
    def empty(self):
        return self.size == 0
    

#%%
# implement queue with stack
class MyQueue:

    def __init__(self):
        self.Instack = Stack()
        self.Outstack = Stack()

    def push(self, x: int) -> None:
        self.Instack.push(x)

    def pop(self) -> int:
        if not self.Outstack.empty():
            val = self.Outstack.pop()
            return val
        while not self.Instack.empty():
            temp = self.Instack.pop()
            self.Outstack.push(temp)
        return self.Outstack.pop()

    def peek(self) -> int:
        if not self.Outstack.empty():
            return self.Outstack.peek()
        while not self.Instack.empty():
            temp = self.Instack.pop()
            self.Outstack.push(temp)
        return self.Outstack.peek()

    def empty(self) -> bool:
        return (self.Instack.getsize() + self.Outstack.getsize()) == 0
 
#%%
my_stack = MyQueue()
my_stack.push(1)
my_stack.push(2)
#print(my_stack.getsize())
print(my_stack.peek())
print(my_stack.pop())
#%%
my_stack.push(3)
print(my_stack.pop())
print(my_stack.peek())
#%%
#print(my_stack.getsize())
print(my_stack.empty())
print(my_stack.pop())
print(my_stack.empty())
#print(my_stack.getsize())      