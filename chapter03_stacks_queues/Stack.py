# LAST IN FIRST OUT

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head:
            tmp = self.head
            while tmp:
                print(tmp.data, " -> ", end="")
                tmp = tmp.next
            print("\n")
        return "Empty stack"

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            tmp = self.head
            self.head = self.head.next
            return tmp
        return False

    def peek(self):
        if self.head:
            return self.head.data

    def is_empty(self):
        return self.head is None



# q = Stack()
# q.push(1)
# q.print()
#
# q.push(2)
# q.push(3)
# q.push(4)
# q.print()
# print("peek: ", q.peek())
#
# print(q.pop().data)
# q.print()
# print("head: ", q.head.data)
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