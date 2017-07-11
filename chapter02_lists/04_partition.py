from ctci.chapter02_lists.LinkedList import LinkedList
from ctci.chapter02_lists.LinkedList import Node

def partition_simple(self, pivot):
    head = self.head
    lower = LinkedList()
    higher = LinkedList()
    while head:
        if head.data <= pivot:
            lower.add(head.data)
        else:
            higher.add(head.data)
        head = head.next
    lower_it = lower.head
    while lower_it:
        higher.add(lower_it.data)
        lower_it = lower_it.next
    return higher


def partition(self, pivot):
# one qsort round
    lp = LinkedList()
    lp.add(pivot)
    pointer = self.head
    while pointer:
        if pointer.data <= pivot:
            lp.add(pointer.data)
        else:
            lp.add_in_the_end(pointer.data)
        pointer = pointer.next
    return lp

ll = LinkedList()
ll.generate(10, 0, 99)
ll.print_list()
(partition_simple(ll, 50)).print_list()
(partition(ll, 50)).print_list()

