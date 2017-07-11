from ctci.chapter02_lists.LinkedList import LinkedList

class Node:
    def __init__(self, value, name):
        self.data = value
        self.name = name
        self.next = None

class AnimalQueue:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.any = LinkedList()

    def enqueue(self, value, name):
        new_node = Node(value, name)
        self.any.add_in_the_end(new_node)
        if value == "cat":
            self.cats.add_in_the_end(new_node)
        elif value == "dog":
            self.dogs.add_in_the_end(new_node)

    def dequeue_any(self):
        popped = self.any.pop()
        if popped.data == "cat":
            self.cats.pop()
        elif popped.data == "dog":
            self.dogs.pop()
        return popped.name

    def dequeue_dog(self):
        popped = self.dogs.pop()
        self.any.remove(popped.name)
        return popped.name

    def dequeue_cat(self):
        popped = self.cats.pop()
        self.any.remove(popped.name)
        return popped.name

q = AnimalQueue()
q.enqueue('cat', 'jasper')
q.enqueue('dog', 'marcel')
q.enqueue('cat', 'alice')
q.enqueue('dog', 'pongo')
q.enqueue('cat', 'nala')
q.enqueue('dog', 'nelly')
q.enqueue('dog', 'rudy')

print(q.dequeue_any())
print(q.dequeue_cat())
print(q.dequeue_dog())
