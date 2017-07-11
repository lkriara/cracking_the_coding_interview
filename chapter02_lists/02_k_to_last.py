from ctci.chapter02_lists.LinkedList import LinkedList

def k_to_last(self, k):
    p1 = self.head
    p2 = self.head.next
    for i in range(k):
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.data

ll = LinkedList()
ll.generate(10, 0, 99)
ll.print_list()
print(k_to_last(ll, 1))
