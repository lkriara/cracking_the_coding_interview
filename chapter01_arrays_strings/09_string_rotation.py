data = [
    ('waterbottle', 'erbottlewat', True),
    ('foo', 'bar', False),
    ('foo', 'foofoo', False)
]

def is_substring(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    diff = length1 - length2 +1
    str1.find(str2)
    first = str1[0]
    new_rotation =[]
    if diff>=1:
        for i in range(length2):
            if str2[i] == first:
                new_rotation = str2[i:] + str2[:i]

        for i in range(diff):
            if set(new_rotation) == set(str1[i:(length1-1-i)]):
                return True
    return False


for row in data:
    # print(row[0])
    # print(row[1])
    # print(row[0].find(row[1]))
    print(is_substring(row[0], row[1]))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False

for row in data:
    print(string_rotation(row[0], row[1]))