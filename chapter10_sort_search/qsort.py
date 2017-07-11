def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    print('first, last', first, last)

    if first < last:
        splitpoint = partition(alist, first, last)
        print(alist[first], alist[splitpoint], alist[last])

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    print(alist)

    pivotvalue = alist[first]
    print('pivot=', pivotvalue)

    leftmark = first + 1
    rightmark = last
    print('in partition', leftmark, rightmark)

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            print('leftmark++', leftmark)

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
            print('rightmark--', rightmark)

        if rightmark < leftmark:
            done = True
        else:
            print('swap in', alist[leftmark], alist[rightmark])
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    print('swap out', alist[first], alist[rightmark])
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
