data = [
    ('Tact Coa', True),
    ('jhsabckuj ahjsbckj', True),
    ('Able was I ere I saw Elba', True),
    ('So patient a nurse to nurse a patient so', False),
    ('Random Words', False),
    ('Not a Palindrome', False),
    ('no x in nixon', True),
    ('azAZ', True)]


def char_to_num(c):
    little_a = ord('a')
    little_z = ord('z')
    capital_a = ord('A')
    capital_z = ord('Z')
    char = ord(c)
    if little_a <= char <= little_z:
        char = char - little_a
    elif capital_a <= char <= capital_z:
        char = char - capital_a
    return char

def how_many_odd(table):
    for i in range(len(table)):
        table[i] = table[i]%2
    if table.count(1)<=1:
        return True
    else:
        return False

def check_palindrome(string):
    table = [0 for _ in range(ord('z') - ord('a') + 1)] #[0 for _ in range(128)]
    for char in string:
        if char != ' ':
            table[char_to_num(char)] = table[char_to_num(char)] + 1
    return how_many_odd(table)

for string in data:
    print("\"", string[0], "\" is a palindrome permutation? -> ", check_palindrome(string[0]))