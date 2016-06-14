from xml.dom.minidom import parse
from dot_structure import dot_structure


def rnaml2dot(name):
    cts = name
    saveName = str(cts).replace('.xml', '(dot)')
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

    with open(saveName, 'w') as f:
        new_file = f.write('>' + main_name + '.dot' + '\n' + seq + '\n' + ''.join(d))
    print("Conversion from (rnaml) to (dot) completed successfully!")


def rnaml2bpseq(name):
    cts = name  # Tworze sobie całe 'drzewo' informacji pliku xml
    saveName = str(cts).replace('.xml', '(bpseq)')
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

    # Uzupełnienie tablicy B o potrzebne zera do metody dot_structure i potem wstawi pary
    X = [0] * len(seq)
    for n, i in zip(A, B):
        X[int(n) - 1] = int(i)
    # jezeli 2 i 10 to para to tez zapisze to jako 10 i 2
    for n, i in zip(B, A):
        X[int(n) - 1] = int(i)

    # Odpowiednik tablicy A tylko cała jest uzupełniona
    Y = []
    for i in range(1, len(seq) + 1):
        Y.append(i)

    output = []

    for i in range(len(seq)):
        output.append("%s%s%s%s%s" % (Y[i], ' ', seq[i], ' ', X[i]))

    with open(saveName, 'w') as f:
        new_file = f.write('>' + main_name + '.bpseq' + '\n' + '\n'.join(output))
    print("Conversion from (rnaml) to (bpseq) completed successfully!")


def rnaml2ct(name):
    cts = name  # Tworze sobie całe 'drzewo' informacji pliku xml
    saveName = str(cts).replace('.xml', '(ct)')
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

    for n, i in zip(B, A):
        X[int(n) - 1] = int(i)

    # Odpowiednik tablicy A tylko cała jest uzupełniona
    Y = []
    for i in range(1, len(seq) + 1):
        Y.append(i)

    output = []

    for i in range(len(seq)):
        output.append("%s%s%s%s%s%s%s%s%s%s%s" % (Y[i], ' ', seq[i], ' ', i, ' ', i + 2, ' ', X[i], ' ', Y[i]))

    with open(saveName, 'w') as f:
        new_file = f.write('>' + main_name + '.ct' + '\n' + '\n'.join(output))
    print("Conversion from (rnaml) to (ct) completed successfully!")
