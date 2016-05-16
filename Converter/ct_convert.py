from dot_structure import dot_structure
import xml.etree.cElementTree as ET


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

    # print (seq)
    # print (''.join(s))
    print('Konwersja przebiegła poprawnie!')

    with open('ct2dot_file', 'w') as d:
        new_file = d.write(title + '.dot' + '\n' + seq + '\n' + ''.join(s))


def ct2rnaml(cts):
    title = cts[0]
    title = title.replace('.bpseq', '')
    title = title.replace('>', '')

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
    tree.write("page.xml")


def ct2bpseq(cts):
    title = cts[0]
    title = title.replace('.ct', '')

    idx = 0
    string = []
    while idx < len(cts):
        line = cts[idx].split()
        if len(line) >= 6 and line[0] == line[5]:
            string.append(line[0] + ' ' + line[1] + ' ' + line[4])
        idx += 1
    # print('\n'.join(string))
    print('Konwersja przebiegła poprawnie!')
    with open('ct2bpseq_file', 'w') as d:
        new_file = d.write(title + '.bpseq' + '\n' + '\n'.join(string))
