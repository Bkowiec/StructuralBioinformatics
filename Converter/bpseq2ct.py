def bpseq2ct(cts):

    title = cts[0]
    title = title.replace('.bpseq', '')

    idx = 0
    string = []
    for i in range(1, len(cts)):
        line = cts[i].split()
        string.append(
            "%d%s%s%s%d%s%d%s%s%s%d" % (i, ' ', line[1], ' ', i - 1, ' ', i + 1, ' ', line[2], ' ', i))
    #print('\n'.join(string))
    print('Konwersja przebiegła poprawnie!')
    with open('bpseq2ct_file', 'w') as d:
        new_file = d.write(title + '.ct' + '\n' + '\n'.join(string))



