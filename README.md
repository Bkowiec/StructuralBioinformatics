# Converter secondary structures of RNA
Converter which can be used to convert between RNA structures formats.

# Supported formats
CT(connet), BPSEQ(basepair), DOT-BRACKET(vienna), RNAML(http://www-lbit.iro.umontreal.ca/rnaml/)<br/>
Pseudoknots are also supported.

# Usage
For example: file with name ,first_seq, in CT format<br/>
In terminal:
```sh
>python main.py first_seq
```
Converter automatically recognizes file format and sets the possible output files:
```sh
Choose save format:
0 - All formats
1 - Dot-bracket
2 - Basepair
3 - RNAML
```
