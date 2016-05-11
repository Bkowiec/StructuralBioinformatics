import re
from dot2ct import dot2ct
from ct2dot import ct2dot
from dot2bpseq import dot2bpseq
from dot_structure import dot_structure
from bpseq2dot import bpseq2dot


try:
    with open('ct2dot_file') as file:
        file_lines = file.read().splitlines()
        title = file_lines[0]

    if re.match(".*.dot", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty'+ '\n' + '1 - Format .ct'+ '\n' + '2 - Format .bpseq' + '\n')

        if x == '0':
            dot2ct(file_lines)
            dot2bpseq(file_lines)
        elif x == '1':
            dot2ct(file_lines)
        elif x == '2':
            dot2bpseq(file_lines)

    if re.match(".*.ct", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty' + '\n' + '1 - Format .dot' + '\n' + '2 - Format .bpseq' + '\n')

        if x == '0':
            ct2dot(file_lines)
        elif x == '1':
            ct2dot(file_lines)
        elif x == '2':
            print('do formatu .bpseq')

    if re.match(".*.bpseq", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty' + '\n' + '1 - Format .ct' + '\n' + '2 - Format .dot' + '\n')

        if x == '0':
            bpseq2dot(file_lines)
        elif x == '1':
            print('do formatu .ct')
        elif x == '2':
            bpseq2dot(file_lines)

except:
    print('Brak wskazanego pliku')