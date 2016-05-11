def ct2bpseq(cts):

    title = cts[0]
    title = title.replace('.ct', '')

    idx = 0
    string=[]
    while idx < len(cts):
        line = cts[idx].split()
        if len(line) >= 6 and line[0] == line[5]:
           string.append(line[0] + ' ' + line[1] + ' ' + line[4])
        idx += 1
    #print('\n'.join(string))
    print('Konwersja przebiegła poprawnie!')
    with open('ct2bpseq_file', 'w') as d:
        new_file = d.write(title + '.bpseq' + '\n' + '\n'.join(string))



