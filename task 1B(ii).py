def flames(name1, name2):
    length = len(name1) + len(name2)

    flames = "F L A M E S"

    count = 0
    while length > 0:
        length -= 1
        if flames[count] != ' ':
            count += 1
    remaining = ''
    for i in range(count):
        remaining += flames[i]
    if remaining == 'F':
        print(name1, 'and', name2, 'are Friends.')
    elif remaining == 'L':
        print(name1, 'and', name2, 'are Lovers.')
    elif remaining == 'A':
        print(name1, 'and', name2, 'are Affectionate.')
    elif remaining == 'M':
        print(name1, 'and', name2, 'are Married.')
    elif remaining == 'E':
        print(name1, 'and', name2, 'are Enemies.')
    elif remaining == 'S':
        print(name1, 'and', name2, 'are Siblings.')
flames('John', 'Sarah')
flames('Tom', 'Jerry')
flames('Robert', 'Julia')