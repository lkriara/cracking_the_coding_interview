class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.min = []

    def print(self):
        if self.head:
            tmp = self.head
            while tmp:
                print(tmp.data, " -> ", end="")
                tmp = tmp.next
            print("\n")
        return "Empty stack"

    def push(self, value):
        if self.head is None:
            self.min.append(value)
            print("length of min array: ", len(self.min))

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.head.data < self.min[len(self.min)-1]:
            self.min.append(self.head.data)
            print("length of min array: ", len(self.min))

    def pop(self):
        if self.head:
            tmp = self.head
            self.head = self.head.next
            if tmp.data == self.min[len(self.min)-1]:
                self.min.remove(tmp.data)
            return tmp
        return False

    def peek(self):
        if self.head:
            return self.head.data

    def find_min(self):
        return self.min[len(self.min)-1]

    def is_empty(self):
        return self.head is None

q = Stack()
q.push(4)
q.print()
print("min: ", q.find_min())

q.push(2)
q.push(3)
q.push(1)
q.print()
print("peek: ", q.peek())

print(q.pop().data)
q.print()
print("min: ", q.find_min())
print("head: ", q.head.data)
# print(q.pop().data)
# q.print()
# print("head: ", q.head.data)
#
# print("-is the stack empty? -", q.is_empty())
#
# print(q.pop().data)
# q.print()
# print("head: ", q.head.data)
# print(q.pop().data)
# q.print()
#
# print("-is the stack empty? -", q.is_empty())