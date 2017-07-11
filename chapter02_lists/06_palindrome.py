from ctci.chapter02_lists.LinkedList import LinkedList
import copy

def is_palindrome_compare(self):
    # reverse list and compare the original and reversed lists
    ordered = self
    reversed = copy.deepcopy(ordered).reverse()
    head = self.head
    rhead = reversed.head
    while head:
        # print(head.data, " ?= ", rhead.data)
        if head.data != rhead.data:
            return False
        head = head.next
        rhead = rhead.next
    return True

def is_palindrome_pop(self):
# add half in a new list (stack) and pop the other half expecting the stack to empty
    stack = []
    p1 = p2 = self.head

    while p2.next:
        stack.append(p1.data)
        p1 = p1.next
        p2 = p2.next.next

    # in case the middle element of the list is single
    if p2:
        p1 = p1.next

    while p1:
        if p1.data != stack.pop():
            return False
        p1 = p1.next
    return True

# def is_palindrome(self):
#     # recursively
#     # TODO



ll_true = LinkedList()
ll_true.add(1)
ll_true.add(2)
ll_true.add(3)
ll_true.add(4)
ll_true.add(5)
ll_true.add(4)
ll_true.add(3)
ll_true.add(2)
ll_true.add(1)
ll_true.print_list()
print(is_palindrome_pop(ll_true))


ll_false = LinkedList()
ll_false.add(1)
ll_false.add(2)
ll_false.add(3)
ll_false.add(4)
ll_false.add(5)
ll_false.add(6)
ll_false.add(7)
ll_false.add(8)
ll_false.add(9)
ll_false.print_list()
print(is_palindrome_pop(ll_false))