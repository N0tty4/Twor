Quando compare l'errore `ERR_NOSUCHSERVER` significa che il parametro `<server>` potrebbe non essere trovato. Il server non dovrebbe mandare alcun comando dopo questo.
Un esempio di parametro potrebbe essere:
```
:Name COMMAND parameter list
```
Un messaggio di questo tipo rappresenta un messaggi che proviene da `Name` in transito tra i server.s
# 4.1 connection registration
Il comando descritto qui è usato per registrare una connessione con un server IRC:
`PASS` commando non è richiesto per i server o per i client, ma deve precedere il messaggio inviato al server. Però è strettamente consigliato che ogni server abbia la sua password. L'ordine raccomandato per registrarsi ad un client è:
- Pass message
- Nick message
- User message
### 4.1.1 Password message
- command: `PASS`
- Parameters: `<password>`
Il comando `PASS` è usato per settare una `password connection`. La password può e deve essere messa prima di ogni registrazione. 
Attualmente è richiesto che un client invii un comando `PASS` prima di inviare il `Nick/User`, e il server deve inviare un `PASS` command prima di ogni comando server.
## 4.1.2 Nick message
- comando: `NICK`
- parameters: `<nickname> [ <hopcount> ]`
è usato per dare ad un utente un nome o cambiare quello precedente. Il `<hopcount>` è usato solo dai server per indicare quando è lontano un nick dal suo home server. Una connessione locale ha `hopcount` di 0.
