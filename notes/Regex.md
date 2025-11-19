Regex sta per ==Regular Expression==, cioè espressione regolare. È una sequenza di caratteri che definisce un pattern di ricerca.
# esempio
Diciamo che vogliamo trovare solo i file con l'estensione `.pdf`. Scrivendo l'espressione
```regex
^\w+\.pdf$
```
funzionerà.
# the period (.)
Il carattere punt `.` CI permette di selezionare ogni carattere, inclusi caratteri speciali e spazzi.
# character sets \[chars\]
Se una parola è diversa dalle altre per solo un carattere, possiamo fare come un ==or== di caratteri che può assumere quella posizione nella parla con:
```regex
word = bar ber bir bor bur
/b[aeiou]r/g
```
cosi da prendere tutte le parola che variano solo per quei carattere in quella posizione.
## negare character sets \[^chars\]
per trovare le parola che non hanno un esatto carattere in una esatta posizione, posiamo fare come per i char set, ma aggiungere `^` all'inizio per indicare cosa non vogliamo che venga trovato:
```regex
word = bar ber bir bor bur
/ b[^eo]r /g
```
cosi si andrà ad escludere `ber, bor`.
# letter range \[a-z\]
Per trovare le lettere in uno specifico range, le lettere iniziali e finali sono scritte tra parentesi, e tra le lettere ci va un trattino. Sono __case sensitive__; includono gli estremi.
```regex
word = abcdefghijklmnopqrstuvwxyz
/ [e-o] /g
result = efghijklmno
```
## numeri \[0-9\]
la stessa regola vale anche per il range di numeri, infatti ci basta mettere il range dal quale far iniziare la nostra ricerca fino a dove farla finire:
```regex
word = 0123456789
/ [3-6] / g
result = 3456
```
# repetitions
Qualche carattere speciale viene usato per specificare quante volte un carattere sarà ripetuto in testo.
Questi caratteri sono:
- +
- *
- ?
## asterisk
se mettiamo un asterisco dopo un carattere, indichiamo che il carattere può non esserci o può esserci una o più volte.
```regex
text = br ber beer
/ be*r /g
result = br ber beer
```
perché la `e` in messo occorre 0 volte o 1 o più volte.
## plus sign
per indicare che un carattere può presentarsi una o più volte, noi mettiamo il segno `+` dopo un carattere. Ad esempio:
```regex
text = br ber beer
/ be+r /g
result = ber beer
```
## question mark
Per indicare che un carattere è opzionale, mettiamo un carattere d'avanti a quel carattere.
```regex
text = color, colour
/ colou?r /g
result = color colour
```
Questo perché la u può esserci come non esserci.
# curly braces
Per esprimere un certo numero di occorrenza dello stesso carattere in sequenza, ci basta mettere dolo il carattere che ci interessa esaminare due parentesi graffe con all'interno il numero di occorrenze che ci interessa
```regex
text = ber beer beeer beeeer beeeeer
/ be{2}r /g
result = beer
```
## range of repetition
Per indicare che vogliamo solo un rage di ripetizione, possiamo mettere 2 numeri tra le parentesi, oppure il numero iniziale e poi niente dopo la virgola per simboleggiare che vogliamo tutti i valori dopo.
```regex
text ? ber beer beeer beeeer beeeeer
/ be{3,}r /g
result = beeer beeeer beeeeer

/ be{1, 3} / g
result = ber, beer, beeer
```
# Parentheses (): grouping
Possiamo raggruppare un'espressione ed usare questi gruppi per riferirci o rinforzare qualche regola. Per farlo possiamo scrivere un'espressione tra parentesi
```regex
text = ha-ha, haa-haa
/ (haa) /g
result = haa haa
```
## referencing a group
Per riferirci ad un gruppo, ci basta indicare il gruppo con (gruppo)-\n dove n indica l'indice del gruppo. Ad esempio:
```regex
text = ha-ha,haa-haa
/ (ha)-\1, (haa)-\2
result = ha-ha,haa-haa
```
## non-capturing grouping
Quando vogliamo togliere qualche gruppo dal conteggio, ci basta
# pipe character
Serve per specificare che un'espressione può essere suddivisa in più espressioni diverse. Questi possibili statements sono separati da una pipe `|`.
# escape character
server per poter selezionare dei caratteri speciali usati per generare le espressioni, come ad esempio `{}, [], (), *, +, .,` ecc...
```regex
text = (*)Asterisk.
/ (\*|\.) /g
reslut = *.
```
# select by line start
il simbolo `^` viene usato anche per indicare che le frasi di ogni linea deve iniziare in una determinata maniera se usata fuori dalle \[\].
```regex
text = "Basic Omellette Recipe
1. 3 eggs, beaten
2. 1 tsp sunflower oil
3. 1 tsp butter"

/ ^[0-9] /gm

result = 1 2 3
```
# dollar sign
il segno del dollaro `$` viene usato per indicare che che la parola che cerchiamo la dobbiamo trovare solo alla fine di una riga
```regex
https://domain.com/what-is-html.|html|
https://otherdomain.com/html-elements
https://website.com/html5-features.|html|

/ html$ /gm
```
# word character
l'espressione `\w` viene usata per trovare lettere, numeri e under_score `_`.
```regex
text = abcABC123_.:-!?
/ \w /g
result = abcABC123_
```
# Except word character
l'espressione `\W` viene usata per indicare l'verso del word character, infatti lui troverà tutto tranne lettere, numeri e \_.
```regex
text = abcABC123_.:-!?
/ \W /g
result = .:!?
```
# Number character
viene usato per trovare solo i numeri `\d`:
```regex
text = abcABC123 .:;!?
/ \d /g
result = 123
```
# Except number character
viene usato per trovare tutto ciò che non è un numero `\D`:
```regex
text = abcABC123 .:;!?
/ \D /g
result = abcABC .:;!?
```
# Space character
viene usato per trovare solo spazi `\s`
# Except space character
viene usato per trovare tutto tranne gli spazzi `\S`
# look-around
Servono per poter prendere dei particolari caratteri che stanno prima o dopo un determinato insieme di caratteri.
## positive look-ahead
se noi vogliamo prendere un determinato elemento prima di una determinata stringa, possiamo usare i ==positive look-ahead== che si esprimono con `(?=)`.
```regex
text = Date: 4 Aug 3PM
/ \d+(?=PM) /g
result = 3
```
## negative look-ahead
Viene usato per selezionare le parole che non hanno uno specifico pattern dopo il dato che ci interessa selezionare. Si indica con `(?!)`
```regex
text = Date: 4 Aug 3PM
/ \d+(?!PM) /g
result = 4
```
## positive look-behind
serve per trovare un gruppo di caratteri dopo un determinato gruppo di caratteri. Si esprime con `(?<=)`
```regex
text = Product Code: 1064 Price: $5
/ (?<=\$)\d+ /g
result = 5
```
## negative look-behind
stessa cosa del positive, ma trova tutti i pattern che non iniziano con un determinato valore.
```regex
text = Product Code: 1064 Price: $5
/ (?<!\$)\d+
result = 1064
```
# flags
cambiano l'output delle nostre espressioni. Questo è anche perché vengono chiamati `modifiers`. Va a modificare quando tratta il testo com linee separate, il case sensitive, o trova tutti i matches.
## global flag
la flag globale causa la selezione di tutte le espressi che fanno il match. Se non usato, troverà solo la prima istanza che fa il match.
```regex
/ \w+\.com /g
```
il `/g` simboleggia la flag globale
## Multi-line flag
Le regex vedono tutto il testo come una sola linea. Ma noi usiamo la flag multi-line per poter separarle. Così che il nostro patter funzionerà per il primo match per ogni riga.
```regex
/ \w+\.com /gm
```
in `/gm`, la `m` simboleggia il multi-line
## case-insensitive flag
serve per poter disabilitare il case-sensitive.
```regex
/ \w+\.com /gmi
```
in `\gmi` la `i` serve per simboleggiare il case-insensitive.
# greedy matching
regex fa un greedy match di default. Significa che il match darà il più lungo possibile.
```regex
text = ber beer beeer beeeer
/ .*r /
```
fa riferimento ad ogni match che finisce con la `r`. Può esserci ogni carattere prima di lui.
# lazy matching
finisce di trovare i match appena ne incontra il primo. Ad esempio, qui sotto viene riportato che si fermerà solo al primo ber
```regex
text = ber beer beeer beeeer
/ .*?r /
result = ber
```
