# Konwerter notacji struktury drugorzędowej RNA
Program umożliwiający dowolną zmianę pomiędzy wybranymi notacjami struktur drugorzędowych. 

# Obsługiwane formaty
CT(connet), BPSEQ(basepair), DOT-BRACKET(vienna), RNAML(http://www-lbit.iro.umontreal.ca/rnaml/)<br/>
Program umożliwia również obsługę rozpoznawanie pseudowęzłów do stopnia dziesiątego.

# Użycie
Po uruchomieniu programu i wskazaniu mu wejściowego pliku, dla przykładu plik o nazwie ,first_seq,<br/>
W terminalu:
```sh
>python main.py first_seq
```
Konwerter automatycznie rozpoznaje format pliku wejściowego i umożliwia wybór formatu pliku wejściowego
```sh
Choose save format:
0 - All formats
1 - Dot-bracket
2 - Basepair
3 - RNAML
```
Po dokonaniu wyboru otrzymamy wygenerowany plik ze zmienionym formatem.<br/>
Gdy konwersja przebiegnie w prawidłowy sposób dostaniemy specjalny komunikat:
```sh
Conversion from (bpseq) to (dot) completed successfully!
```
