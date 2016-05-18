def dot_structure(A, B):
    # structure = numpy.repeat('.', len(A))
    structure = ['.'] * len(A)
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []
    s7 = []
    s8 = []
    s9 = []
    s10 = []
    s11 = []

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

        if len(s5) == 0:
            s5.append(b)
            structure[a - 1] = 'A'
            structure[b - 1] = 'a'
            continue
        elif (a < s5[len(s5) - 1]) & (b > s5[len(s5) - 1]):
            pass
        else:
            s5.append(b)
            structure[a - 1] = 'A'
            structure[b - 1] = 'a'
            continue

        if len(s6) == 0:
            s6.append(b)
            structure[a - 1] = 'B'
            structure[b - 1] = 'b'
            continue
        elif (a < s6[len(s6) - 1]) & (b > s6[len(s6) - 1]):
            pass
        else:
            s6.append(b)
            structure[a - 1] = 'B'
            structure[b - 1] = 'b'
            continue

        if len(s7) == 0:
            s7.append(b)
            structure[a - 1] = 'C'
            structure[b - 1] = 'c'
            continue
        elif (a < s7[len(s7) - 1]) & (b > s7[len(s7) - 1]):
            pass
        else:
            s7.append(b)
            structure[a - 1] = 'C'
            structure[b - 1] = 'c'
            continue

        if len(s8) == 0:
            s8.append(b)
            structure[a - 1] = 'D'
            structure[b - 1] = 'd'
            continue
        elif (a < s8[len(s8) - 1]) & (b > s8[len(s8) - 1]):
            pass
        else:
            s8.append(b)
            structure[a - 1] = 'D'
            structure[b - 1] = 'd'
            continue

        if len(s9) == 0:
            s9.append(b)
            structure[a - 1] = 'E'
            structure[b - 1] = 'e'
            continue
        elif (a < s9[len(s9) - 1]) & (b > s9[len(s9) - 1]):
            pass
        else:
            s9.append(b)
            structure[a - 1] = 'E'
            structure[b - 1] = 'e'
            continue

        if len(s10) == 0:
            s10.append(b)
            structure[a - 1] = 'F'
            structure[b - 1] = 'f'
            continue
        elif (a < s10[len(s10) - 1]) & (b > s10[len(s10) - 1]):
            pass
        else:
            s10.append(b)
            structure[a - 1] = 'F'
            structure[b - 1] = 'f'
            continue

        if len(s11) == 0:
            s11.append(b)
            structure[a - 1] = 'G'
            structure[b - 1] = 'g'
            continue
        elif (a < s11[len(s11) - 1]) & (b > s11[len(s11) - 1]):
            pass
        else:
            s11.append(b)
            structure[a - 1] = 'G'
            structure[b - 1] = 'g'
            continue

    return structure
    # return structure.toString()
