import numpy

def arithmetic_shift(x, count):
    for i in range(count):
        x >>= 1
        # print("temp x for count: ", i, " is -> ", x)
    return x

def logical_shift(x, count):
    if x>=0:
        return x >> count
    else:
        return (x & 0xffffffff) >> count

x = -93242
count = 40

print("x= ", x, ", count= ", count)
print("x= ", bin(x), ", length: ", len(bin(x)))
print("arithmetic_shift: ", arithmetic_shift(x, count))
print("operator : ", x>>count)
print("inbuilt: ", numpy.right_shift(x, count))

print("logical_shift function: ", logical_shift(x, count))
print("logical shift for negatives: ", (x & 0xffffffff) >> count)
