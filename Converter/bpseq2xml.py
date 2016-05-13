import xml.etree.cElementTree as ET

def bpseq2rnaml(cts):
    title = cts[0]
    title = title.replace('.bpseq', '')

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

    root = ET.Element("base-pair")
    elo = ET.SubElement(root, "seq-data")
    root.set("name", title)
    elo.text = seq
    for a, b in zip(A, B):
        basep5 = ET.SubElement(root, "base-id-p5")
        baseidp5 = ET.SubElement(basep5, "base-id")
        position5 = ET.SubElement(baseidp5, "position")
        position5.text = str(a)

        basep3 = ET.SubElement(root, "base-id-p3")
        baseidp3 = ET.SubElement(basep3, "base-id")
        position3 = ET.SubElement(baseidp3, "position")
        position3.text = str(b)

    tree = ET.ElementTree(root)
    tree.write("page.xml")
