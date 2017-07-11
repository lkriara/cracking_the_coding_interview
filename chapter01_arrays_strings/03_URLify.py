data = [(list('much ado about nothing      '), 22, list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

for string in data:
    print(string[0])
    print("\n")

    gaps = string[0].count(' ')/3
    length = len(string[0])-1

    i = string[1]-1
    while i >= 0:
        if string[0][i] != ' ':
            string[0][length] = string[0][i]
            length = length - 1
        else:
            string[0][length] = '0'
            string[0][length-1] = '2'
            string[0][length-2] = '%'

            length = length - 3
            gaps -= 1

        if gaps == 0:
            break
        i -= 1

    print(string[0])
    print(string[2])