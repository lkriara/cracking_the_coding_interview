from ctci.chapter02_lists.LinkedList import LinkedList

def remove_dups(self):
    head = self.head
    index = set()
    index.add(head.data)
    while head.next:
        if head.next.data not in index:
            index.add(head.next.data)
            head = head.next
        else:
            # self.remove(head.data)
            head.next = head.next.next

def remove_dups_followup(self):
#     two pointers, compare each item with all of them O(N^2)
    p1 = self.head
    while p1:
        p2 = p1
        while p2.next:
            if p1.data == p2.next.data:
                # self.remove(p2.data)
                p2.next = p2.next.next
            else:
                p2 = p2.next
        p1 = p1.next
    return self.head


ll = LinkedList()
ll.generate(10, 0, 4)
ll.print_list()
remove_dups(ll)
ll.print_list()

ll1 = LinkedList()
ll1.generate(10, 0, 4)
ll1.print_list()
remove_dups_followup(ll1)
ll1.print_list()
