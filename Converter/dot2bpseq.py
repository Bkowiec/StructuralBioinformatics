def dot2bpseq(file_lines):
    title = file_lines[0]
    title = title.replace('.dot', '')
    seq = file_lines[1]
    str = file_lines[2]

    ctstring = []
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    stack10 = []
    stack11 = []

    pairs = {}

    for i, c in enumerate(str):
        if c == '(':
            stack1.append(i + 1)
        elif c == '[':
            stack2.append(i + 1)
        elif c == '{':
            stack3.append(i + 1)
        elif c == '<':
            stack4.append(i + 1)
        elif c == 'A':
            stack5.append(i + 1)
        elif c == 'B':
            stack6.append(i + 1)
        elif c == 'C':
            stack7.append(i + 1)
        elif c == 'D':
            stack8.append(i + 1)
        elif c == 'E':
            stack9.append(i + 1)
        elif c == 'F':
            stack10.append(i + 1)
        elif c == 'G':
            stack11.append(i + 1)
        elif c == ')':
            pairs[i + 1] = stack1.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == ']':
            pairs[i + 1] = stack2.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == '}':
            pairs[i + 1] = stack3.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == '>':
            pairs[i + 1] = stack4.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'a':
            pairs[i + 1] = stack5.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'b':
            pairs[i + 1] = stack6.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'c':
            pairs[i + 1] = stack7.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'd':
            pairs[i + 1] = stack8.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'e':
            pairs[i + 1] = stack9.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'f':
            pairs[i + 1] = stack10.pop()
            pairs[pairs[i + 1]] = i + 1
        elif c == 'g':
            pairs[i + 1] = stack11.pop()
            pairs[pairs[i + 1]] = i + 1

    for i in range(1, len(str) + 1):
        ctstring.append("%d%s%s%s%d" % (i, ' ', seq[i - 1], ' ', pairs.get(i, 0)))
    #print(title)
    #print('\n'.join(ctstring))
    print('Konwersja przebiegła poprawnie!')

    with open('dot2bpseq_file', 'w') as d:
        new_file = d.write(title + '.bpseq' + '\n' + '\n'.join(ctstring))
