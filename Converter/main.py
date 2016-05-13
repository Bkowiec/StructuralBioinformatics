import re
from dot2ct import dot2ct
from ct2dot import ct2dot
from dot2bpseq import dot2bpseq
from dot_structure import dot_structure
from bpseq2dot import bpseq2dot
from ct2bpseq import ct2bpseq
from bpseq2ct import bpseq2ct
from bpseq2xml import bpseq2rnaml
from ct2xml import ct2rnaml
from dot2xml import dot2xml

try:
    with open('3') as file:
        file_lines = file.read().splitlines()
        title = file_lines[0]

    if re.match(".*.dot", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty'+ '\n' + '1 - Format .ct'+ '\n' + '2 - Format .bpseq' + '\n' + '3 - Format .RNAML' + '\n')

        if x == '0':
            dot2ct(file_lines)
            dot2bpseq(file_lines)
        elif x == '1':
            dot2ct(file_lines)
        elif x == '2':
            dot2bpseq(file_lines)
        elif x == '3':
            dot2xml(file_lines)

    if re.match(".*.ct", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty' + '\n' + '1 - Format .dot' + '\n' + '2 - Format .bpseq' + '\n' + '3 - Format .RNAML' + '\n')

        if x == '0':
            ct2dot(file_lines)
            ct2bpseq(file_lines)
        elif x == '1':
            ct2dot(file_lines)
        elif x == '2':
            ct2bpseq(file_lines)
        elif x == '3':
            ct2rnaml(file_lines)

    if re.match(".*.bpseq", title):
        x = input('Wybierz format zapisu:' + '\n' + '0 - Wszystkie formaty' + '\n' + '1 - Format .ct' + '\n' + '2 - Format .dot' + '\n' + '3 - Format RNAML' + '\n')

        if x == '0':
            bpseq2dot(file_lines)
            bpseq2ct(file_lines)
            bpseq2rnaml(file_lines)
        elif x == '1':
            bpseq2ct(file_lines)
        elif x == '2':
            bpseq2dot(file_lines)
        elif x == '3':
            bpseq2rnaml(file_lines)

except:
    print('Brak wskazanego pliku')