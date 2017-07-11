from ctci.chapter02_lists.LinkedList import LinkedList

def intersect(ll1, ll2):
    h1 = ll1.head
    h2 = ll2.head

    while h1:
        while h2:
            if h1 == h2:
                return True
            h2 = h2.next
        h1 = h1.next
    return False


ll1 = LinkedList()
ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)
ll1.add(4)
ll1.add(3)
ll1.add(2)
ll1.add(1)
ll1.print_list()


ll2 = LinkedList()
ll2.add(1)
ll2.add(2)
ll2.add(3)
ll2.add(4)
ll2.add_node(ll1.head)
ll2.add(5)
ll2.add(6)
ll2.add(7)
ll2.add(8)
ll2.add(9)
ll2.print_list()

print(intersect(ll1, ll2))