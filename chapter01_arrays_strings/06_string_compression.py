data = [('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')]

for string in data:
    original_length = len(string[0])
    # print(original_length)
    compressed = []
    i=0
    prev = string[0][i]
    cnt = 0
    # idx = 0
    while i<original_length:
        if string[0][i] == prev:
            cnt += 1
        else:
            # compressed.insert(idx, prev)
            # compressed.insert(idx+1, cnt)
            compressed.append(prev + str(cnt))
            # print("insert ", prev, " at idx = ", idx)
            prev = string[0][i]
            cnt = 1
            # idx += 2
        # print("i = ", i, " - char = ", string[0][i], " - count = ", cnt)
        i += 1
    # compressed.insert(idx, prev)
    # compressed.insert(idx + 1, cnt)
    compressed.append(prev + str(cnt))

    # # compare new length to original_length
    # if len(compressed) >= original_length:
    #     print(string[0])
    # else:
    #     print(compressed)
    print(min(string[0], compressed, key=len))
