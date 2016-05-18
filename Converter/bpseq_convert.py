import xml.etree.cElementTree as ET
from dot_structure import dot_structure
import re

def bpseq2ct(cts):
    title = ">seq_name.ct"
    if re.match(r">.*.bpseq", cts[0]):
        title = cts[0]
        title = title.replace('.bpseq', '.ct')

    idx = 0
    string = []


    input_form = []
    for x in range(0, len(cts)):
        if re.match("\s*\d+\s+[A-Z]\s+\d+(?!\s)", cts[x]):
            input_form.append(cts[x])

    for i in range(1, len(input_form)):
        line = input_form[i].split()
        string.append(
            "%d%s%s%s%d%s%d%s%s%s%d" % (i, ' ', line[1], ' ', i - 1, ' ', i + 1, ' ', line[2], ' ', i))
    # print('\n'.join(string))


    with open('bpseq2ct_file', 'w') as d:
        new_file = d.write(title + '\n' + '\n'.join(string))
    print("Conversion from (.bpseq) to (.ct) completed successfully!")


def bpseq2dot(cts):
    title = ">seq_name.dot"
    if re.match(r">.*.bpseq", cts[0]):
        title = cts[0]
        title = title.replace('.bpseq', '.dot')

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

    # print(seq)
    # print(''.join(s))

    with open('bpseq2dot_file', 'w') as d:
        new_file = d.write(title + '\n' + seq + '\n' + ''.join(s))
    print("Conversion from (.bpseq) to (.dot) completed successfully!")


def bpseq2rnaml(cts):
    title = "seq_name"
    if re.match(r">.*.bpseq", cts[0]):
        title = cts[0]
        title = title.replace('.bpseq', '').replace('>', '')

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

    rnaml = ET.Element("rnaml")
    molecule = ET.SubElement(rnaml, "molecule")
    identity = ET.SubElement(molecule, "identity")
    name = ET.SubElement(identity, "name")
    name.text = str(title)
    sequence = ET.SubElement(molecule, "sequence")
    sequence.set("length", str(len(seq)))
    seq_data = ET.SubElement(sequence, "seq-data")
    seq_data.text = seq
    structure = ET.SubElement(molecule, "structure")

    for a, b in zip(A, B):
        if b > a:
            base_pair = ET.SubElement(structure, "base-pair")

            basep5 = ET.SubElement(base_pair, "base-id-p5")
            baseidp5 = ET.SubElement(basep5, "base-id")
            position5 = ET.SubElement(baseidp5, "position")
            position5.text = str(a)

            basep3 = ET.SubElement(base_pair, "base-id-p3")
            baseidp3 = ET.SubElement(basep3, "base-id")
            position3 = ET.SubElement(baseidp3, "position")
            position3.text = str(b)

    tree = ET.ElementTree(rnaml)
    tree.write("bpseq2rnaml.xml")
    print("Conversion from (.bpseq) to (.xml) completed successfully!")
