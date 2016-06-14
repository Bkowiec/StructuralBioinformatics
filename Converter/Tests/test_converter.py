import unittest
from os.path import sep, isfile
from os import getcwd, remove
from dot_convert import dot2ct, dot2bpseq, dot2rnaml
from ct_convert import ct2bpseq, ct2rnaml, ct2dot
from bpseq_convert import bpseq2ct, bpseq2rnaml, bpseq2dot
from rnaml_convert import rnaml2dot, rnaml2bpseq, rnaml2ct


class DotConverterTests(unittest.TestCase):
    def test_dot2ct(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">mouseSeq.dot"]
        cts = [
            "CAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGA",
            "..(((((...(((((...(((((...(((((.....)))))...))))).....(((((...(((((.....)))))...))))).....)))))...))))).."
        ]
        file_1 = open("seq3(ct)").read()
        dot2ct(cts, title, file_path)
        file_path += "(ct)"
        file_2 = open("seq-test(ct)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_dot2bpseq(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">mouseSeq.dot"]
        cts = [
            "CAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGA",
            "..(((((...(((((...(((((...(((((.....)))))...))))).....(((((...(((((.....)))))...))))).....)))))...))))).."
        ]
        file_1 = open("seq3(bpseq)").read()
        dot2bpseq(cts, title, file_path)
        file_path += "(bpseq)"
        file_2 = open("seq-test(bpseq)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_dot2rnaml(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">mouseSeq.dot"]
        cts = [
            "CAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGA",
            "..(((((...(((((...(((((...(((((.....)))))...))))).....(((((...(((((.....)))))...))))).....)))))...))))).."
        ]
        file_1 = open("seq3.xml").read()
        dot2rnaml(cts, title, file_path)
        file_path += ".xml"
        file_2 = open("seq-test.xml").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_FailDot2ct(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">mouseSeq.dot"]
        cts = [
            "CAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGACAGCACGACACUAGCAGUCAGUGUCAGACUGCAGA",
            "..(((((...(((((...()))))...))))).....)))))...))))).."
        ]
        dot2ct(cts, title, file_path)
        file_path += "(ct)"
        self.assertFalse(isfile(file_path))

    def test_fixedDot2ct(self):
        file_path = getcwd() + sep + "Fixit"
        file_path2 = getcwd() + sep + "Fixed"
        title = [">mouseSeq.dot"]
        title2 = [">mouseSeq.ct"]
        cts = [
            "GAAGUACAAUAUGUAACCG",
            ".(.{{((.....)))}}.."
        ]
        cts2 = [
            "1 G 0 2 0 1",
            "2 A 1 3 15 2",
            "3 A 2 4 0 3",
            "4 G 3 5 17 4",
            "5 U 4 6 16 5",
            "6 A 5 7 14 6",
            "7 C 6 8 13 7",
            "8 A 7 9 0 8",
            "9 A 8 10 0 9",
            "10 U 9 11 0 10",
            "11 A 10 12 0 11",
            "12 U 11 13 0 12",
            "13 G 12 14 7 13",
            "14 U 13 15 6 14",
            "15 A 14 16 2 15",
            "16 A 15 17 5 16",
            "17 C 16 18 4 17",
            "18 C 17 19 0 18",
            "19 G 18 20 0 19"
        ]
        dot2ct(cts, title, file_path)
        file_path += "(ct)"
        self.assertTrue(isfile(file_path))
        ct2dot(cts2, title2, file_path2)


class CtConverterTests(unittest.TestCase):
    def test_ct2dot(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.ct"]
        cts = [
            "1 A 0 2 0 1",
            "2 G 1 3 10 2",
            "3 A 2 4 0 3",
            "4 U 3 5 12 4",
            "5 G 4 6 0 5",
            "6 A 5 7 14 6",
            "7 C 6 8 0 7",
            "8 G 7 9 16 8",
            "9 C 8 10 0 9",
            "10 A 9 11 2 10",
            "11 U 10 12 0 11",
            "12 A 11 13 4 12",
            "13 C 12 14 0 13",
            "14 G 13 15 6 14",
            "15 U 14 16 0 15",
            "16 A 15 17 8 16",
            "17 C 16 18 0 17"
        ]
        file_1 = open("seq2(dot)").read()
        ct2dot(cts, title, file_path)
        file_path += "(dot)"
        file_2 = open("seq-test(dot)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_ct2bpseq(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.ct"]
        cts = [
            "1 A 0 2 0 1",
            "2 G 1 3 10 2",
            "3 A 2 4 0 3",
            "4 U 3 5 12 4",
            "5 G 4 6 0 5",
            "6 A 5 7 14 6",
            "7 C 6 8 0 7",
            "8 G 7 9 16 8",
            "9 C 8 10 0 9",
            "10 A 9 11 2 10",
            "11 U 10 12 0 11",
            "12 A 11 13 4 12",
            "13 C 12 14 0 13",
            "14 G 13 15 6 14",
            "15 U 14 16 0 15",
            "16 A 15 17 8 16",
            "17 C 16 18 0 17"
        ]
        file_1 = open("seq2(bpseq)").read()
        ct2bpseq(cts, title, file_path)
        file_path += "(bpseq)"
        file_2 = open("seq-test(bpseq)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_ct2rnaml(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.ct"]
        cts = [
            "1 A 0 2 0 1",
            "2 G 1 3 10 2",
            "3 A 2 4 0 3",
            "4 U 3 5 12 4",
            "5 G 4 6 0 5",
            "6 A 5 7 14 6",
            "7 C 6 8 0 7",
            "8 G 7 9 16 8",
            "9 C 8 10 0 9",
            "10 A 9 11 2 10",
            "11 U 10 12 0 11",
            "12 A 11 13 4 12",
            "13 C 12 14 0 13",
            "14 G 13 15 6 14",
            "15 U 14 16 0 15",
            "16 A 15 17 8 16",
            "17 C 16 18 0 17"
        ]
        file_1 = open("seq2.xml").read()
        ct2rnaml(cts, title, file_path)
        file_path += ".xml"
        file_2 = open("seq-test.xml").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_failCt2dot(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.ct"]
        cts = [
            "6 A 0 2 0 1",
            "2 G 1 3 10 2",
            "5 A 2 4 0 3",
            "4 U 3 5 12 4",
            "5 G 4 6 0 5",
            "6 A 0 0 0 0",
            "7 C 6 8 0 7",
            "8 G 7 9 16 8",
            "9 C 8 10 0 9",
            "10  2 10 9 9",
            "11 U 10 12 0 11",
            "12 A 1 12 0 0",
            "13 C 12 14 0 13",
            "34 G 13 15 6 14",
            "15 U 14 16 0 15",
            "17 C 16 18 0 17"
        ]
        ct2dot(cts, title, file_path)
        file_path += "(dot)"
        self.assertFalse(isfile(file_path))


class BpseqConverterTests(unittest.TestCase):
    def test_bpseq2dot(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.bpseq"]
        cts = [
            "1 A 0",
            "2 G 10",
            "3 A 0",
            "4 U 12",
            "5 G 0",
            "6 A 14",
            "7 C 0",
            "8 G 16",
            "9 C 0",
            "10 A 2",
            "11 U 0",
            "12 A 4",
            "13 C 0",
            "14 G 6",
            "15 U 0",
            "16 A 8",
            "17 C 0"
        ]
        file_1 = open("seq1(dot)").read()
        bpseq2dot(cts, title, file_path)
        file_path += "(dot)"
        file_2 = open("seq-test(dot)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_bpseq2ct(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.bpseq"]
        cts = [
            "1 A 0",
            "2 G 10",
            "3 A 0",
            "4 U 12",
            "5 G 0",
            "6 A 14",
            "7 C 0",
            "8 G 16",
            "9 C 0",
            "10 A 2",
            "11 U 0",
            "12 A 4",
            "13 C 0",
            "14 G 6",
            "15 U 0",
            "16 A 8",
            "17 C 0"
        ]
        file_1 = open("seq1(ct)").read()
        bpseq2ct(cts, title, file_path)
        file_path += "(ct)"
        file_2 = open("seq-test(ct)").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_bpseq2rnaml(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.bpseq"]
        cts = [
            "1 A 0",
            "2 G 10",
            "3 A 0",
            "4 U 12",
            "5 G 0",
            "6 A 14",
            "7 C 0",
            "8 G 16",
            "9 C 0",
            "10 A 2",
            "11 U 0",
            "12 A 4",
            "13 C 0",
            "14 G 6",
            "15 U 0",
            "16 A 8",
            "17 C 0"
        ]
        file_1 = open("seq1.xml").read()
        bpseq2rnaml(cts, title, file_path)
        file_path += ".xml"
        file_2 = open("seq-test.xml").read()
        self.assertTrue(isfile(file_path))
        self.assertEqual(file_1, file_2)
        remove(file_path)

    def test_failBpseq2dot(self):
        file_path = getcwd() + sep + "seq-test"
        title = [">niceOne.bpseq"]
        cts = [
            "0 A 0",
            "2 G 10",
            "3 A 0",
            "4 U 12",
            "6 A 15",
            "7 C 0",
            "8 G 16",
            "9 C 0",
            "10 A 2",
            "11 U 0",
            "54 Z 4",
            "14 G 6",
            "15 U 0",
            "16 A 8",
            "17 C 0"
        ]
        bpseq2dot(cts, title, file_path)
        file_path += "(dot)"
        self.assertFalse(isfile(file_path))


if __name__ == '__main__':
    unittest.main()
