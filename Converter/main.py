import re
import sys
import os
from bpseq_convert import bpseq2ct, bpseq2rnaml, bpseq2dot
from ct_convert import ct2bpseq, ct2rnaml, ct2dot
from dot_convert import dot2ct, dot2bpseq, dot2rnaml
from rnaml_convert import rnaml2dot, rnaml2bpseq, rnaml2ct

connect = "\s*\d+\s+[A-Z]\s+\d+\s+\d+\s+\d+\s+\d+"
base_pair = "\s*\d+\s+[A-Z]\s+\d+(?!\s)"
dot_form = "[A-Z]+"
bracket_form = "[\.\<\[\{\(\)\>\]\}]{2}"
input_form = []
dot = []
bracket = []

try:
    with open("LOL1") as file:
        file_lines = file.read().splitlines()
        title = file_lines[0]
        file_name = file.name

    if re.match(".*.xml", file_name):
        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Dot-bracket (.dot)' + '\n' + '3 - Basepair (.bpseq)' + '\n')

        if x == '0':
            rnaml2dot(file.name)
            rnaml2bpseq(file.name)
            rnaml2ct(file.name)
        elif x == '1':
            rnaml2ct(file.name)
        elif x == '2':
            rnaml2dot(file.name)
        elif x == '3':
            rnaml2bpseq(file.name)
    elif re.match(r">.*.(ct|bpseq|dot)", title):
        if re.match(".*.dot", title):
            x = input(
                'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Basepair (.bpseq)' + '\n' + '3 - RNAML (.XML)' + '\n')
            try:
                if x == '0':
                    dot2ct(file_lines)
                    dot2bpseq(file_lines)
                    dot2rnaml(file_lines)
                elif x == '1':
                    dot2ct(file_lines)
                elif x == '2':
                    dot2bpseq(file_lines)
                elif x == '3':
                    dot2rnaml(file_lines)
            except:
                print("Invalid input format")
        if re.match("(.*.ct)", title):
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
    else:
        if re.findall(connect, str(file_lines)):
            for x in range(0, len(file_lines)):
                if re.match(connect, file_lines[x]):
                    input_form.append(file_lines[x])
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
        elif re.findall(base_pair, str(file_lines)):
            for x in range(0, len(file_lines)):
                if re.match(base_pair, file_lines[x]):
                    input_form.append(file_lines[x])
            x = input(
                'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Dot-bracket (.dot)' + '\n' + '3 - RNAML (.XML)' + '\n')

            if x == '0':
                bpseq2dot(input_form)
                bpseq2ct(input_form)
                bpseq2rnaml(input_form)
            elif x == '1':
                bpseq2ct(input_form)
            elif x == '2':
                bpseq2dot(input_form)
            elif x == '3':
                bpseq2rnaml(input_form)
        elif re.findall(bracket_form, str(file_lines)):
            for x in range(0, len(file_lines)):
                if re.match(dot_form, file_lines[x]):
                    dot.append(file_lines[x])
                elif re.match(bracket_form, file_lines[x]):
                    bracket.append(file_lines[x])
            for x in dot:
                t = 0
                while t < len(bracket):
                    if len(x) == len(bracket[t]):
                        input_form.append(x)
                        input_form.append(bracket[t])
                    t += 1
            x = input(
                'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Basepair (.bpseq)' + '\n' + '3 - RNAML (.XML)' + '\n')
            try:
                if x == '0':
                    dot2ct(input_form)
                    dot2bpseq(input_form)
                    dot2rnaml(input_form)
                elif x == '1':
                    dot2ct(input_form)
                elif x == '2':
                    dot2bpseq(input_form)
                elif x == '3':
                    dot2rnaml(input_form)
            except:
                print("Invalid input format")
except:
    print('File not found')
