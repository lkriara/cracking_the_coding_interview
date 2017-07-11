# from ctci.chapter02_lists.llist_implementation import sllist, llist
from ctci.chapter02_lists.LinkedListClasses import LinkedList

def reverse(x):
    for i in range(int(len(x)/2)):
        x[i], x[len(x)-1-i] = x[len(x)-1-i], x[i]
    print(x)

# x = sllist([0, 1, 2, 3, 4, 5, 6]);
# print(x)
# reverse(x)
# print(x)


ll = LinkedList();
ll.generate(10, 0, 9)
print(ll)
ll.reverse()

print(ll)



