È una libreria di python che serve per __semplificare__ la codifica delle __command-line interfaces__.
- Il programma definisce quali argomenti verranno richiesti, ed `argparse` penserà a come analizzarli four da `sys.argv`
- genera automaticamente messaggi di __help__, di __aiuto__ e individua errori quando l'utente immette argomenti invalidi.
# funzionamento
Il supporto per il modulo `argparse` è costruito attorno un' interfaccia di `argparse.ArgumentParser`. È un contenitore per le specificazioni degli argomenti ed ha dei `options`.
```python
import argparse
parser = argparse.ArgumentParser(
	prog = 'ProgramName'
	description = 'what the program does',
	epilog = 'text at the bottom of help')
```
# `ArgumrntParser.addargument()`
È un metodo che crea argomenti di specifiche individuali per il parser. Supporta argomenti posizionali, opzioni che accettano valori e flag on/of.
```python
parser.add_argument('filename')
parser.add_argument('-c', '--count')
parser.add_argument('-v', '--verbose'
	action='store_true')
```
# `ArgumentParser.parse_args()`
Esegue il parser e posiziona il dato estratto in un oggetto `argparse.Namespace`.
```python
args = parser.parse_args()
print(args.filename, args.count, args.verbose)
```

