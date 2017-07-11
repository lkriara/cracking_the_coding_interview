str = [(['abcd', 'bacd']), (['3563476', '7334566']), (['wef34f', 'wffe34']),                       # True
       (['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f']), (['123', '1234'])]           # False

def permutation(str1, str2):
    if len(str1) == len(str2):
        str_tab = [0 for _ in range(128)]

        for char in str1:
            str_tab[ord(char)] = str_tab[ord(char)] + 1
        for char in str2:
            if str_tab[ord(char)] == 0:
                return False
            str_tab[ord(char)] = str_tab[ord(char)] - 1
        return True
    else:
        return False


for string_pair in str:
    print(permutation(string_pair[0], string_pair[1]))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import Counter

def perm_solution_given(string):
    str1 = string[0]
    str2 = string[1]
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


# for test_string in str:
#     print(perm_solution_given(test_string))