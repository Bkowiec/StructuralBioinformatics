# Konwerter notacji struktury drugorzędowej RNA
Program umożliwiający dowolną zmianę pomiędzy wybranymi notacjami struktur drugorzędowych. 

# Obsługiwane formaty
CT(connet), BPSEQ(basepair), DOT-BRACKET(vienna), RNAML(http://www-lbit.iro.umontreal.ca/rnaml/)<br/>
Program umożliwia również obsługę rozpoznawania pseudowęzłów do rzędu dziesiątego.

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

# Poprawność plików
W przypadku gdy pliki są przez nas przygotowane, powinny mieć kostrukcję, w której wskazujemy na jedną z notacji. Wtedy zakładamy, że wprowadzony plik jest poprawny. Jednak gdy plik jest wygenerowany przez inny program lub nie jest przez nas przygotowany, konwerter automatycznie szuka jaki format został użyty i wykonuje się. Gdy dane uniemożliwiają wykonanie się programu, program informuje nas o tym.
<br/>
<br/>
Connect:
```sh
>first_seq.ct
1 A 0 2 0 1
2 G 1 3 10 2
3 U 2 4 0 3
4 C 3 5 12 4
5 G 4 6 0 5
6 C 5 7 14 6
7 A 6 8 0 7
8 U 7 9 16 8
9 G 8 10 0 9
10 C 9 11 2 10
11 A 10 12 0 11
12 U 11 13 4 12
13 G 12 14 0 13
14 C 13 15 6 14
15 A 14 16 0 15
16 G 15 17 8 16
17 C 16 18 0 17
```
Basepair:
```sh
>first_seq.bpseq
1 A 0
2 G 10
3 U 0
4 C 12
5 G 0
6 C 14
7 A 0
8 U 16
9 G 0
10 C 2
11 A 0
12 U 4
13 G 0
14 C 6
15 A 0
16 G 8
17 C 0
```
Dot-bracket:
```sh
>first_seq.dot
AGUCGCAUASKDSKALG
.(.[.{.<.).].}.>.
```
RNAML:
```sh
<rnaml>
	<molecule>
		<identity>
			<name>seq_name</name>
		</identity>
		<sequence length="17">
			<seq-data>AGUCGCAUGCAUGCAGC</seq-data>
		</sequence>
		<structure>
			<base-pair>
				<base-id-p5>
					<base-id>
						<position>2</position>
					</base-id>
				</base-id-p5>
				<base-id-p3>
					<base-id>
						<position>10</position>
					</base-id>
				</base-id-p3>
			</base-pair>
			<base-pair>
				<base-id-p5>
					<base-id>
						<position>4</position>
					</base-id>
				</base-id-p5>
				<base-id-p3>
					<base-id>
						<position>12</position>
					</base-id>
				</base-id-p3>
			</base-pair>
			<base-pair>
				<base-id-p5>
					<base-id>
						<position>6</position>
					</base-id>
				</base-id-p5>
				<base-id-p3>
					<base-id>
						<position>14</position>
					</base-id>
				</base-id-p3>
			</base-pair>
			<base-pair>
				<base-id-p5>
					<base-id>
						<position>8</position>
					</base-id>
				</base-id-p5>
				<base-id-p3>
					<base-id>
						<position>16</position>
					</base-id>
				</base-id-p3>
			</base-pair>
		</structure>
	</molecule>
</rnaml>
```







