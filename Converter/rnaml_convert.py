from xml.dom.minidom import parse
from dot_structure import dot_structure


def rnaml2dot():
    cts = "page.xml"
    # Tworze sobie całe 'drzewo' informacji pliku xml
    dom = parse(cts)
    seq_data = dom.getElementsByTagName('seq-data')
    name = dom.getElementsByTagName('name')
    main_name = name[0].firstChild.nodeValue
    seq = seq_data[0].firstChild.nodeValue.replace(' ', '').replace('\n', '')
    base_pair = dom.getElementsByTagName('base-pair')
    seq_length = dom.getElementsByTagName('sequence')
    tmp = seq_length[0]
    length_seq = tmp.attributes["length"]
    A = []
    B = []

    # Wyłuskiwanie z tagów BASE-PAIR tagów POSITION a z nich textu
    i = 0
    for x in base_pair:
        position = base_pair[i].getElementsByTagName('position')
        A.append(position[0].firstChild.nodeValue)
        B.append(position[1].firstChild.nodeValue)
        i += 1

    # Uzupełnienie tablicy B o potrzebne zera do metody dot_structure
    X = [0] * len(seq)
    for n, i in zip(A, B):
        X[int(n) - 1] = int(i)

    # Odpowiednik tablicy A tylko cała jest uzupełniona
    Y = []
    for i in range(1, len(seq) + 1):
        Y.append(i)

    d = dot_structure(Y, X)

    print(main_name)
    print(seq)
    print(''.join(d))

    with open('rnaml2dot_file', 'w') as f:
        new_file = f.write(main_name + '\n' + seq + '\n' + ''.join(d))


def rnaml2bpseq():
    cts = "page.xml"  # Tworze sobie całe 'drzewo' informacji pliku xml
    dom = parse(cts)
    seq_data = dom.getElementsByTagName('seq-data')
    name = dom.getElementsByTagName('name')
    main_name = name[0].firstChild.nodeValue
    seq = seq_data[0].firstChild.nodeValue.replace(' ', '').replace('\n', '')
    base_pair = dom.getElementsByTagName('base-pair')
    seq_length = dom.getElementsByTagName('sequence')
    tmp = seq_length[0]
    length_seq = tmp.attributes["length"]
    A = []
    B = []

    # Wyłuskiwanie z tagów BASE-PAIR tagów POSITION a z nich textu
    i = 0
    for x in base_pair:
        position = base_pair[i].getElementsByTagName('position')
        A.append(position[0].firstChild.nodeValue)
        B.append(position[1].firstChild.nodeValue)
        i += 1

    # Uzupełnienie tablicy B o potrzebne zera do metody dot_structure
    X = [0] * len(seq)
    for n, i in zip(A, B):
        X[int(n) - 1] = int(i)

    # Odpowiednik tablicy A tylko cała jest uzupełniona
    Y = []
    for i in range(1, len(seq) + 1):
        Y.append(i)

    output = []

    for i in range(len(seq)):
        output.append("%s%s%s%s%s" % (Y[i], ' ', seq[i], ' ', X[i]))

    with open('rnaml2bpseq_file', 'w') as f:
        new_file = f.write('\n'.join(output))


def rnaml2ct():
    cts = "page.xml"  # Tworze sobie całe 'drzewo' informacji pliku xml
    dom = parse(cts)
    seq_data = dom.getElementsByTagName('seq-data')
    name = dom.getElementsByTagName('name')
    main_name = name[0].firstChild.nodeValue
    seq = seq_data[0].firstChild.nodeValue.replace(' ', '').replace('\n', '')
    base_pair = dom.getElementsByTagName('base-pair')
    seq_length = dom.getElementsByTagName('sequence')
    tmp = seq_length[0]
    length_seq = tmp.attributes["length"]
    A = []
    B = []

    # Wyłuskiwanie z tagów BASE-PAIR tagów POSITION a z nich textu
    i = 0
    for x in base_pair:
        position = base_pair[i].getElementsByTagName('position')
        A.append(position[0].firstChild.nodeValue)
        B.append(position[1].firstChild.nodeValue)
        i += 1

    # Uzupełnienie tablicy B o potrzebne zera do metody dot_structure
    X = [0] * len(seq)
    for n, i in zip(A, B):
        X[int(n) - 1] = int(i)

    # Odpowiednik tablicy A tylko cała jest uzupełniona
    Y = []
    for i in range(1, len(seq) + 1):
        Y.append(i)

    output = []

    for i in range(len(seq)):
        output.append("%s%s%s%s%s%s%s%s%s%s%s" % (Y[i], ' ', seq[i], ' ', i, ' ', i + 2, ' ', X[i], ' ', Y[i]))

    with open('rnaml2ct_file', 'w') as f:
        new_file = f.write('\n'.join(output))
