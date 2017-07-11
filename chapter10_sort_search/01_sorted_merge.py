from random import randint

def merge_sorted(a, b):
    len_a = len(a)
    len_b = len(b)

    i = len_a - len_b - 1
    print("len_b = ", len_b, ", i = ", i)
    while i>0:
        print("in while")
        while len_b>0:
            if b[len_b-1] > a[i]:
                a[len_a-1] = b[len_b-1]
                a[len_a-2] = a[i]
                print("a[", len_a-1, "] = ", b[len_b-1])
                print("a[", len_a-2, "] = ", a[i])
            else:
                # a[len_a - 1] = a[i]
                # a[len_a - 2] = b[len_b-1]
                # print("a[", len_a - 1, "] = ", a[i])
                # print("a[", len_a - 2, "] = ", b[len_b - 1])
            len_b -= 1
            len_a -= 2
        i -= 1

    return a


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

len_a = 5
buffer = 3
len_b = 3

A = [0 for _ in range(len_a+buffer)]
B = [0 for _ in range(len_b)]

for i in range(len_a):
    A[i] = i*2 + 1

for i in range(len_b):
    B[i] = i*5 + 3

print(A)
print(B)

print(merge_sorted(A, B))