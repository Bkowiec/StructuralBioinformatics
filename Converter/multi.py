import re

from dot_convert import dot2ct, dot2bpseq, dot2rnaml


def multil(cts, title, file_name):
    dot_form = "[AUGC]{2,}"
    bracket_form = "[\.\<\[\{\(\)\>\]\}\s]{2,}"
    finally_form = []
    dot = []
    bracket = []
    title = title
    file_name = file_name

    for x in range(0, len(cts)):
        if re.match(dot_form, cts[x]):
            dot.append(re.match(dot_form, cts[x]).group())
        elif re.match(bracket_form, cts[x]):
            bracket.append(re.match(bracket_form, cts[x]).group())

    if len(dot) == len(bracket):
        finally_form.append(''.join(dot))
        finally_form.append(''.join(bracket))

        x = input(
            'Choose save format:' + '\n' + '0 - All formats' + '\n' + '1 - Connect (.ct)' + '\n' + '2 - Basepair (.bpseq)' + '\n' + '3 - RNAML (.XML)' + '\n')
        try:
            if x == '0':
                dot2ct(finally_form, title, file_name)
                dot2bpseq(finally_form, title, file_name)
                dot2rnaml(finally_form, title, file_name)
            elif x == '1':
                dot2ct(finally_form, title, file_name)
            elif x == '2':
                dot2bpseq(finally_form, title, file_name)
            elif x == '3':
                dot2rnaml(finally_form, title, file_name)
        except:
            print("Invalid input format")
    else:
        print("Invalid input format")
