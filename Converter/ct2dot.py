from dot_structure import dot_structure
def ct2dot(cts):

    title = cts[0]
    title = title.replace('.ct', '')


    A = []
    B = []
    seq = ''

    idx = 0
    while idx < len(cts):
        line = cts[idx].split()
        if len(line) >= 6 and line[0] == line[5]:
            if line[5] == '1':  # first line
                A = [int(line[0])]
                B = [int(line[4])]
                seq += line[1]
            else:
                A.append(int(line[0]))
                B.append(int(line[4]))
                seq += line[1]
        idx += 1
    if len(A) > 0:
        s = dot_structure(A, B)

    #print (seq)
    #print (''.join(s))
    print('Konwersja przebiegła poprawnie!')

    with open('ct2dot_file', 'w') as d:
        new_file = d.write(title + '.dot' + '\n' + seq + '\n' + ''.join(s) )
