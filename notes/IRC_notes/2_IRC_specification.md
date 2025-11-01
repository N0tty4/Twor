Il protocollo is può usare sia per `server to server` che `client to server connections`.
# 2.2 character codes
Non è specificato nessun character set; il protocollo si basa su un insieme di codice che sono composti da 8 bits. Alcuni di questi ottetti sono usati come control codes, che funzionano come delimitatori di messaggi.
La particolarità è che prende \{\} e | come lower case di \[\] e \ per le sue origini scandinave.
# 2.3 messages
I server ed i client generano messaggi i quali possono o non possono generare una risposta.
Se il messaggio contiene un __comando valido__ allora il client dovrebbe aspettarsi una risposta; ma non bisogna aspettare per sempre nel ricevere una risposta; __client to server e server to client__ sono per natura __asincrone__.
## parti del messaggio IRC
Sono principalmente composti da __tre parti__:
- il prefisso (opzionale)
- il comando
- i parametri del comando (possono essere fino a 15)
- il prefisso, comando e i parametri sono separati da (`0x20`), (spazio)
### prefisso:
- la presenza di un prefisso è indicato con un singolo carattere ASCII (`:`), 
- il quale dovrà essere il primo carattere in assoluto
- non ci devono essere spazzi tra esso e `: (0x3b)`
Viene usato dal server per indicare l'origine del messaggio. Se manca viene assunto che provenga da chi l'hai inviato prima.
I client __non devono usare il prefisso per inviare i messaggi__, o se lo fanno devono mettere come il __loro nickname__.
Se il __source__ non può essere trovato nel database, se è differente dal collegamento fornito dal messaggio, allora sarà silenziosamente ignorato.
I comandi devono essere o dei __validi comandi IRC__ o __tree caratteri numerici rappresentati in ASCII text__.
### terminazione IRC message
IRC messages sono sempre linee di caratteri che finiscono con `CR-LF` o meglio con `\r\n`. Questi messaggi non devono essere più grandi di ==512 caratteri==, compresi anche di `\r\n`.
## 2.3.1 Message format pseudo BNF
Il messaggio protocollare deve essere estratto dal continuo flusso di ottetti. La soluzione migliore è di mettere `\r\n` come separatore. I __messaggi vuoti sono ignorati__.
Il messaggio estratto può essere suddiviso in (come detto prima) in:
- prefisso
- comando
- lista di parametri
```BNF
<message>  ::= [':' <prefix> <space ] <command> <params> <crlf>
<prefix>   ::= <servername> | <nick> [ '!' <user> ] ['@' <host> ]
<command>  ::= <letter> ( <letter> ) | <number> <number> <number>
<space>    ::= ' '
<middle>   ::= ongi sequenza non vuoto di ottetti, la quale prima non                 deve essere ':'
<trailing> ::= ogni possibile sequenza, possibilmente vuota non                       includendo NUL or CR o LF
<crlf>     ::= CR LF
```
### note
1. gli spazzi non comprendono i `tab`
2. dopo l'estrazione dei parametri dalla lista, tutti i parametri sono uguali, uno non dipende dall'altro.
3. `NUL` character is not special in message farming, basically could end up inside a parameter; is not allowed within messages.
4. l'ultimo parametro potrebbe essere una stringa vuota
5. l'uso del prefisso `['!' <user> ] ['@' <host> ]` deve non essere usato in server to server communications, ma sono in server-to-client communication per dare le informazioni adeguate.
## 2.4 numeric replies
La maggior parte dei messaggi inviati al server generano un reply di qualche tipo. I più comuni sono i reply numerici. Non è concesso originarli da un da un client, infatti vengono silenziosamente ignorati.
