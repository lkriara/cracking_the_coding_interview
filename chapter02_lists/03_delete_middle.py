from ctci.chapter02_lists.LinkedList import LinkedList

def find_middle_element(self):
    p1 = self.head
    p2 = self.head.next

    while p2.next:
        p1 = p1.next
        p2 = p2.next.next

    return p1.data

def delete_middle_element(self, k):
    p1 = self.head
    tmp = self.head
    for i in range(k):
        p1 = p1.next

    while p1.next:
        if p1.next.next is None:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
        p1 = p1.next


ll = LinkedList()
ll.generate(10, 0, 99)
ll.print_list()
print(find_middle_element(ll))

delete_middle_element(ll, 5)
ll.print_list()