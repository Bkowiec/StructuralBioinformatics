import re
import os
from bpseq_convert import bpseq2ct, bpseq2rnaml, bpseq2dot
from ct_convert import ct2bpseq, ct2rnaml, ct2dot
from dot_convert import dot2ct, dot2bpseq, dot2xml
from rnaml_convert import rnaml2dot

tmp = ''

try:
    with open('rnaml2bpseq_file') as file:
        dupa = file
        file_lines = file.read().splitlines()
        title = file_lines[0]
    tmp = 'ok'
except:
    print('File not found')

if tmp == 'ok':

    if re.match(".*.dot", title):
        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Basepair (.bpseq)' + '\n' + '3 - RNAML (.XML)' + '\n')

        if x == '0':
            dot2ct(file_lines)
            dot2bpseq(file_lines)
            dot2xml(file_lines)
        elif x == '1':
            dot2ct(file_lines)
        elif x == '2':
            dot2bpseq(file_lines)
        elif x == '3':
            dot2xml(file_lines)

    if re.match(".*.ct", title):
        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Dot-bracket (.dot)' + '\n' + '2 - Basepair (.bpseq)' + '\n' + '3 - RNAML (.XML)' + '\n')

        if x == '0':
            ct2dot(file_lines)
            ct2bpseq(file_lines)
            ct2rnaml(file_lines)
        elif x == '1':
            ct2dot(file_lines)
        elif x == '2':
            ct2bpseq(file_lines)
        elif x == '3':
            ct2rnaml(file_lines)

    if re.match(".*.bpseq", title):
        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Dot-bracket (.dot)' + '\n' + '3 - RNAML (.XML)' + '\n')

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

    if re.match(".rnaml.", title):
        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Dot-bracket (.dot)' + '\n' + '3 - Basepair (.bpseq)' + '\n')

        if x == '0':
            print(':)')
        elif x == '1':
            print(':)')
        elif x == '2':
            print(':)')
        elif x == '3':
            print(':)')

