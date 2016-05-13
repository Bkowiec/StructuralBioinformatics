import xml.etree.cElementTree as ET
def dot2xml(file_lines):
    title = file_lines[0]
    title = title.replace('.dot', '')
    seq = file_lines[1]
    pattern = file_lines[2]


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
    root = ET.Element("base-pair")
    elo = ET.SubElement(root, "seq-data")
    root.set("name", title)
    elo.text = seq
    for i in range(1, len(pattern) + 1):
        basep5 = ET.SubElement(root, "base-id-p5")
        baseidp5 = ET.SubElement(basep5, "base-id")
        position5 = ET.SubElement(baseidp5, "position")
        position5.text = str(i)

        basep3 = ET.SubElement(root, "base-id-p3")
        baseidp3 = ET.SubElement(basep3, "base-id")
        position3 = ET.SubElement(baseidp3, "position")
        position3.text = str(pairs.get(i, 0))
    tree = ET.ElementTree(root)
    tree.write("page.xml")



