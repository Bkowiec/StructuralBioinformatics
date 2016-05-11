from dot_structure import dot_structure


def bpseq2dot(cts):
    title = cts[0]
    title = title.replace('.bpseq', '')

    A = []
    B = []
    seq = ''

    idx = 0
    while idx < len(cts):
        line = cts[idx].split()
        if len(line) >= 3:
            if line[1] == '1':
                A = [int(line[0])]
                B = [int(line[2])]
                seq += line[1]
            else:
                A.append(int(line[0]))
                B.append(int(line[2]))
                seq += line[1]
        idx += 1
    if len(A) > 0:
        s = dot_structure(A, B)

    print(seq)
    print(''.join(s))
    # print s

    with open('bpseq2dot_file', 'w') as d:
        new_file = d.write(title + '.dot' + '\n' + seq + '\n' + ''.join(s))
