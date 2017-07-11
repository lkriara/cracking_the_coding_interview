class MultiStack:
    def __init__(self, stacksize):
        self.stack_no = 3
        self.array = [0] * (stacksize * self.stack_no)
        self.each_stack_size = [0] * self.stack_no
        self.arraysize = stacksize

    def push(self, value, stack_id):
        if self.is_full(stack_id):
            return "stack full"
        self.each_stack_size[stack_id] += 1
        self.array[self.top_index(stack_id)] = value
        return

    def pop(self, stack_id):
        if self.is_empty(stack_id):
            return "empty stack"
        val = self.array[self.top_index(stack_id)]
        self.array[self.top_index(stack_id)] = 0
        self.each_stack_size[stack_id] -= 1
        return val

    def is_full(self, stack_id):
        return self.each_stack_size[stack_id] == self.arraysize

    def is_empty(self, stack_id):
        return self.each_stack_size[stack_id] == 0

    def top_index(self, stack_id):
        return self.each_stack_size[stack_id] * stack_id -1

# array_id = 1
# array_length = 9
# no_array = 3
# for i in range(0,21,no_array):
#     print((i + array_id) % array_length)

ms = MultiStack(4)  # size 4 for each of the 3 stacks

print("-is stack ", 1, " empty? - ", ms.is_empty(1))
ms.push(1,1)
print("top index: ", ms.top_index(1))
ms.push(2,1)
print("-is stack ", 1, " empty? - ", ms.is_empty(1))
ms.push(3,1)
ms.push(4,1)
print("top index: ", ms.top_index(1))
print("popped: ", ms.pop(1))
print("-is stack ", 1, " full? - ", ms.is_full(1))


print("-is stack ", 0, " empty? - ", ms.is_empty(0))
ms.push(1,0)
print("top index: ", ms.top_index(0))
ms.push(2,0)
print("-is stack ", 0, " empty? - ", ms.is_empty(0))
ms.push(3,0)
ms.push(4,0)
print("top index: ", ms.top_index(0))
print("-is stack ", 0, " full? - ", ms.is_full(0))
