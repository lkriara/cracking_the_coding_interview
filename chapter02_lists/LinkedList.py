from random import randint

class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, " -> ", end="")
            tmp = tmp.next
        print("\n")

    def add(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def add_in_the_end(self, value):
        new_node = Node(value, None)
        if self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node
        else:
            self.head = new_node

    def add_node(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        tmp = self.head
        self.head = tmp.next
        self.head.next = tmp.next.next
        return tmp.data

    def get_node(self, index):
        h = self.head
        while h.next and index>0:
            h = h.next
            index -= 1
        return h

    def size(self):
        counter = 0
        head = self.head
        while head:
            counter += 1
            head = head.next
        return counter

    def remove(self, node):
        tmp = self.head
        if tmp.data == node:
            self.head = tmp.next
            return
        while tmp.next is not None:
            if tmp.next.data is node:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

    def reverse(self):
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return self

    def generate(self, items_no, min_val, max_val):
        for i in range(items_no):
            self.add(randint(min_val, max_val))
        return self

# ll = LinkedList()
# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.print_list()
# ll.remove(3)
# ll.print_list()

#
# ll.generate(5, 32, 64)
# ll.print_list()
#
# ll.reverse()
# ll.print_list()