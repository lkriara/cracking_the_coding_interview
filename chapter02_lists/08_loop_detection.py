from ctci.chapter02_lists.LinkedList import LinkedList

def find_loop(ll):
    p1 = p2 = ll.head
    loop = False
    while p1 and p2:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            print("Collision Node: ", p1.data)  # K = k mod Loopsize -> is k nodes from the loop start
            # p2 is k steps in loop already
            # p1 entered loop in k steps from head
            collision_node = p1
            # return True
            loop = True
            break

    if loop:
        index = 0
        p2 = ll.head
        while p2 is not collision_node:
            p2 = p2.next
            collision_node = collision_node.next
            index+=1
        return p2.data

    return False


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)
ll.add(9)
ll.add(10)
ll.add(11)
ll.add(12)
ll.add(13)
print("Start of the Loop: ", ll.get_node(4).data)
ll.add_node(ll.get_node(4))
print("Starting Loop Node has value: ", find_loop(ll))

ll1 = LinkedList()
ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
print("Starting Loop Node has value: ", find_loop(ll1))

# ll.print_list()