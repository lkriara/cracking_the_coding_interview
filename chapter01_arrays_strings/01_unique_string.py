str = [('abcd'), ('s4fad'), (''), ('23ds2'), ('hb 627jh=j ()')]
# print(len(str))

for string in str:
    if len(string)<128:
        print(string)
        char_table = [False for _ in range(128)]
        flag = 0
        for char in string:
            # print(ord(char))
            if char_table[ord(char)]:
                print("False")
                flag = 1
                break
            char_table[ord(char)] = True
        if not flag:
            print("True")
