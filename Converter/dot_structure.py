def dot_structure(A, B):
    # structure = numpy.repeat('.', len(A))
    structure = ['.'] * len(A)
    s1 = []
    s2 = []
    s3 = []
    s4 = []

    for a, b in zip(A, B):
        # print ('a:', a, 'b:', b)

        if a > b:
            continue

        if len(s1) == 0:
            s1.append(b)
            structure[a - 1] = '('
            structure[b - 1] = ')'
            continue
        elif (a < s1[len(s1) - 1]) & (b > s1[len(s1) - 1]):
            pass
        else:
            s1.append(b)
            structure[a - 1] = '('
            structure[b - 1] = ')'
            continue

        if len(s2) == 0:
            s2.append(b)
            structure[a - 1] = '['
            structure[b - 1] = ']'
            continue
        elif (a < s2[len(s2) - 1]) & (b > s2[len(s2) - 1]):
            pass
        else:
            s2.append(b)
            structure[a - 1] = '['
            structure[b - 1] = ']'
            continue

        if len(s3) == 0:
            s3.append(b)
            structure[a - 1] = '{'
            structure[b - 1] = '}'
            continue
        elif (a < s3[len(s3) - 1]) & (b > s3[len(s3) - 1]):
            pass
        else:
            s3.append(b)
            structure[a - 1] = '{'
            structure[b - 1] = '}'
            continue

        if len(s4) == 0:
            s4.append(b)
            structure[a - 1] = '<'
            structure[b - 1] = '>'
            continue
        elif (a < s4[len(s4) - 1]) & (b > s4[len(s4) - 1]):
            pass
        else:
            s4.append(b)
            structure[a - 1] = '<'
            structure[b - 1] = '>'
            continue

    return structure
    # return structure.toString()
