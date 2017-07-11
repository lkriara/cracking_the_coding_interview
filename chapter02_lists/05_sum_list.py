from ctci.chapter02_lists.LinkedList import LinkedList

def sum_lists(ll1, ll2):
    pass_on = 0;
    h1 = ll1.head
    h2 = ll2.head
    sum_list = LinkedList()
    while h1.next or h2.next:
        if h2.next is None:
            ll2.add_in_the_end(0)
        elif h1.next is None:
            ll1.add_in_the_end(0)
        h1 = h1.next
        h2 = h2.next
    # ll1.print_list()
    # ll2.print_list()

    h1 = ll1.head
    h2 = ll2.head
    while h1 and h2:
        # print(pass_on, " + ", h1.data, " + ", h2.data, "%10 = ", (pass_on + h1.data + h2.data)%10)
        sum_list.add((pass_on + h1.data + h2.data)%10)
        pass_on = (h1.data + h2.data)//10
        h1 = h1.next
        h2 = h2.next
    if pass_on>0:
        sum_list.add(pass_on)
    return sum_list.reverse()

# TODO
def sum_lists_followup(ll1, ll2):
    tmp_sum = 0
    h1 = ll1.head
    h2 = ll2.head
    sum_list = LinkedList()
    while h1.next or h2.next:
        if h2.next is None:
            ll2.add(0)
            h1 = h1.next
        elif h1.next is None:
            ll1.add(0)
            h2 = h2.next
        else:
            h1 = h1.next
            h2 = h2.next
    # ll1.print_list()
    # ll2.print_list()

    h1 = ll1.head
    h2 = ll2.head
    i = 0
    while h1.next and h2.next:
        # print(h1.data, " + ", h2.data, " = ", h1.data + h2.data, "  -  10x when i=", i, " = ", 10**i)
        tmp_sum += (10**i)*(h1.data + h2.data)
        h1 = h1.next
        h2 = h2.next
        i += 1
    # print("sum = ", tmp_sum)

    for i in str(tmp_sum):
        sum_list.add(int(i))

    return sum_list


ll_a = LinkedList()
ll_a.generate(5, 1, 9)
ll_a.print_list()
ll_b = LinkedList()
ll_b.generate(3, 1, 9)
ll_b.print_list()
(sum_lists(ll_a, ll_b)).print_list()

print("")

ll_c = LinkedList()
ll_c.generate(4, 1, 9)
ll_c.print_list()
ll_d = LinkedList()
ll_d.generate(3, 1, 9)
ll_d.print_list()
(sum_lists_followup(ll_c, ll_d)).print_list()
