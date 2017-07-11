from ctci.chapter03_stacks_queues.Stack import Stack

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return
        return self.stacks[len(self.stacks)-1]

    # def is_full(self):
    #     return self.stacks[stack_id] == self.arraysize

    def push(self, value):
        last_stack = Stack()
        last_stack = self.get_latest_stack()
        if last_stack.is_full():
            new_stack = Stack()
            new_stack.push(value)
            self.stacks.append(new_stack)
        else:
            last_stack.push(value)
        return

    def pop(self):
        last_stack = Stack()
        last_stack = self.get_last_stack()
        if last_stack:
            return last_stack.pop()
            if last_stack.is_empty():
                self.stacks.remove(last_stack)
        return

    def pop_at(self, index):
        stack_idx = Stack()
        stack_idx = self.stacks[index]
        popped = stack_idx.pop()
        if stack_idx.is_empty():
            self.stacks.remove(stack_idx)
        # elif len(self.stacks) > index + 1:
        for i in range(index+1, len(self.stacks), 1):
            stack_idx.push(self.stacks[i].pop())
            stack_idx = self.stacks[i]
        return  popped