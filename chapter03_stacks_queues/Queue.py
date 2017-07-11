# FIRST IN FIRST OUT

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def print(self):
        if self.first:
            tmp = self.first
            while tmp:
                print(tmp.data, " -> ", end="")
                tmp = tmp.next
            print("\n")
        return "Empty queue"

    def add(self, value):
        new_node = Node(value)
        if self.last:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first:
            tmp = self.first
            self.first = self.first.next
            return tmp

        return False

    def is_empty(self):
        return self.first is None


q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.print()
print("first: ", q.first.data, " - last: ", q.last.data)

print(q.remove().data)
q.print()
print("first: ", q.first.data, " - last: ", q.last.data)
print(q.remove().data)
q.print()
print("first: ", q.first.data, " - last: ", q.last.data)

print("-is the queue empty? -", q.is_empty())

print(q.remove().data)
q.print()
print("first: ", q.first.data, " - last: ", q.last.data)
print(q.remove().data)
q.print()
# print("first: ", q.first.data, " - last: ", q.last.data)

print("-is the queue empty? -", q.is_empty())