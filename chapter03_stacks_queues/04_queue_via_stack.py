from ctci.chapter03_stacks_queues.Stack import Stack

class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, value):
        self.in_stack.push(value)

    def pop(self):
        while self.in_stack.is_empty() is False:
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
