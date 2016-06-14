import xml.etree.cElementTree as ET
import re


def dot2ct(cts, input_title, file_name):
    try:
        if re.match(">.*.dot", input_title[0]):
            title = input_title[0]
            title = title.replace('.dot', '.ct')
        else:
            title = ">seq_name.ct"

        seq = cts[0]
        pattern = cts[1]

        ctstring = []
        stack1 = []
        stack2 = []
        stack3 = []
        stack4 = []
        stack5 = []
        stack6 = []
        stack7 = []
        stack8 = []
        stack9 = []
        stack10 = []
        stack11 = []
        pairs = {}

        for i, c in enumerate(pattern):
            if c == '(':
                stack1.append(i + 1)
            elif c == '[':
                stack2.append(i + 1)
            elif c == '{':
                stack3.append(i + 1)
            elif c == '<':
                stack4.append(i + 1)
            elif c == 'A':
                stack5.append(i + 1)
            elif c == 'B':
                stack6.append(i + 1)
            elif c == 'C':
                stack7.append(i + 1)
            elif c == 'D':
                stack8.append(i + 1)
            elif c == 'E':
                stack9.append(i + 1)
            elif c == 'F':
                stack10.append(i + 1)
            elif c == 'G':
                stack11.append(i + 1)
            elif c == ')':
                pairs[i + 1] = stack1.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == ']':
                pairs[i + 1] = stack2.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '}':
                pairs[i + 1] = stack3.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '>':
                pairs[i + 1] = stack4.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'a':
                pairs[i + 1] = stack5.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'b':
                pairs[i + 1] = stack6.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'c':
                pairs[i + 1] = stack7.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'd':
                pairs[i + 1] = stack8.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'e':
                pairs[i + 1] = stack9.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'f':
                pairs[i + 1] = stack10.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'g':
                pairs[i + 1] = stack11.pop()
                pairs[pairs[i + 1]] = i + 1

        for i in range(1, len(pattern) + 1):
            ctstring.append(
                "%d%s%s%s%d%s%d%s%d%s%d" % (i, ' ', seq[i - 1], ' ', i - 1, ' ', i + 1, ' ', pairs.get(i, 0), ' ', i))
        # print(title)
        # print('\n'.join(ctstring))

        with open(file_name + '(ct)', 'w') as d:
            new_file = d.write(title + '\n' + '\n'.join(ctstring))
        print("Conversion from (dot) to (ct) completed successfully!")
    except:
        print("Invalid input format")


def dot2bpseq(cts, input_title, file_name):
    try:
        if re.match(">.*.dot", input_title[0]):
            title = input_title[0]
            title = title.replace('.dot', '.bpseq')
        else:
            title = ">seq_name.bpseq"

        seq = cts[0]
        pattern = cts[1]

        ctstring = []
        stack1 = []
        stack2 = []
        stack3 = []
        stack4 = []
        stack5 = []
        stack6 = []
        stack7 = []
        stack8 = []
        stack9 = []
        stack10 = []
        stack11 = []

        pairs = {}

        for i, c in enumerate(pattern):
            if c == '(':
                stack1.append(i + 1)
            elif c == '[':
                stack2.append(i + 1)
            elif c == '{':
                stack3.append(i + 1)
            elif c == '<':
                stack4.append(i + 1)
            elif c == 'A':
                stack5.append(i + 1)
            elif c == 'B':
                stack6.append(i + 1)
            elif c == 'C':
                stack7.append(i + 1)
            elif c == 'D':
                stack8.append(i + 1)
            elif c == 'E':
                stack9.append(i + 1)
            elif c == 'F':
                stack10.append(i + 1)
            elif c == 'G':
                stack11.append(i + 1)
            elif c == ')':
                pairs[i + 1] = stack1.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == ']':
                pairs[i + 1] = stack2.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '}':
                pairs[i + 1] = stack3.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '>':
                pairs[i + 1] = stack4.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'a':
                pairs[i + 1] = stack5.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'b':
                pairs[i + 1] = stack6.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'c':
                pairs[i + 1] = stack7.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'd':
                pairs[i + 1] = stack8.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'e':
                pairs[i + 1] = stack9.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'f':
                pairs[i + 1] = stack10.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'g':
                pairs[i + 1] = stack11.pop()
                pairs[pairs[i + 1]] = i + 1

        for i in range(1, len(pattern) + 1):
            ctstring.append("%d%s%s%s%d" % (i, ' ', seq[i - 1], ' ', pairs.get(i, 0)))
        # print(title)
        # print('\n'.join(ctstring))

        with open(file_name + '(bpseq)', 'w') as d:
            new_file = d.write(title + '\n' + '\n'.join(ctstring))
        print("Conversion from (dot) to (bpseq) completed successfully!")
    except:
        print("Invalid input format")


def dot2rnaml(cts, input_title, file_name):
    try:
        if re.match(">.*.dot", input_title[0]):
            title = input_title[0]
            title = title.replace('.dot', '').replace('>', '')
        else:
            title = "seq_name"

        seq = cts[0]
        pattern = cts[1]

        stack1 = []
        stack2 = []
        stack3 = []
        stack4 = []
        stack5 = []
        stack6 = []
        stack7 = []
        stack8 = []
        stack9 = []
        stack10 = []
        stack11 = []
        pairs = {}

        for i, c in enumerate(pattern):
            if c == '(':
                stack1.append(i + 1)
            elif c == '[':
                stack2.append(i + 1)
            elif c == '{':
                stack3.append(i + 1)
            elif c == '<':
                stack4.append(i + 1)
            elif c == 'A':
                stack5.append(i + 1)
            elif c == 'B':
                stack6.append(i + 1)
            elif c == 'C':
                stack7.append(i + 1)
            elif c == 'D':
                stack8.append(i + 1)
            elif c == 'E':
                stack9.append(i + 1)
            elif c == 'F':
                stack10.append(i + 1)
            elif c == 'G':
                stack11.append(i + 1)
            elif c == ')':
                pairs[i + 1] = stack1.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == ']':
                pairs[i + 1] = stack2.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '}':
                pairs[i + 1] = stack3.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == '>':
                pairs[i + 1] = stack4.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'a':
                pairs[i + 1] = stack5.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'b':
                pairs[i + 1] = stack6.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'c':
                pairs[i + 1] = stack7.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'd':
                pairs[i + 1] = stack8.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'e':
                pairs[i + 1] = stack9.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'f':
                pairs[i + 1] = stack10.pop()
                pairs[pairs[i + 1]] = i + 1
            elif c == 'g':
                pairs[i + 1] = stack11.pop()
                pairs[pairs[i + 1]] = i + 1

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

        for i in range(1, len(pattern) + 1):
            if i < pairs.get(i, 0):
                base_pair = ET.SubElement(structure, "base-pair")

                basep5 = ET.SubElement(base_pair, "base-id-p5")
                baseidp5 = ET.SubElement(basep5, "base-id")
                position5 = ET.SubElement(baseidp5, "position")
                position5.text = str(i)

                basep3 = ET.SubElement(base_pair, "base-id-p3")
                baseidp3 = ET.SubElement(basep3, "base-id")
                position3 = ET.SubElement(baseidp3, "position")
                position3.text = str(pairs.get(i, 0))

        tree = ET.ElementTree(rnaml)
        tree.write(file_name + ".xml")
        print("Conversion from (dot) to (rnaml) completed successfully!")
    except:
        print("Invalid input format")
