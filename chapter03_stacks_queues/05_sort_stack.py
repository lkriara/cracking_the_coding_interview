from ctci.chapter03_stacks_queues.Stack import Stack

def sort_stack(stack):
    tmp_stack = Stack()

    while not stack.is_empty():
        val = stack.pop().data
        while not tmp_stack.is_empty():
            if val < tmp_stack.peek():
                # print("val (", val, ") < tmp_stack.peek() (", tmp_stack.peek(), ")")
                tmp = tmp_stack.pop().data
                stack.push(tmp)
            else:
                break
        tmp_stack.push(val)

    #     print("tmp_stack : ", end="")
    #     tmp_stack.print()
    #     print("stack : ", end="")
    #     stack.print()
    #
    # print("stack is empty? -", stack.is_empty())

    while not tmp_stack.is_empty():
        # val = tmp_stack.pop().data
        # print("val pushed back is ", val)
        # stack.push(val)
        stack.push(tmp_stack.pop().data)
    # print("stack end: ", end="")
    # stack.print()


q = Stack()
q.push(12)
q.push(52)
q.push(32)
q.push(465)
q.print()

sort_stack(q)
q.print()
