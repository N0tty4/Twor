è stato implementato come mezzo per mettere agli utenti collegati a una ==BBS (Bulletin Board System)== di chattare in tempo reale.
L'idea era quella di poter far parlare gli utenti in tempo reale al posto di postare in bacheca le loro conversazioni.
## concetti base
IRC (Internet Relay Chat) protocol è stato sviluppato usando i protocolli TCP/IP. è un sistema di teleconferenza che funziona sul modello __client-server__.
# 1.1 servers
I server formano la struttura del IRC, fornendo 
- Un punto da cui i client possono connettersi e parlare
- Un punto sul quale gli altri server si possono connettere formando un network IRC
L'unico modello di network concesso è il ==spanning tree==: ogni server funziona come un nodo centrale per il resto del network.
## 1.2 clients
Un client è tutto quello che è connesso ad un server che non è un server.
Ogni client è distinto dagli altri per:
- nickname, massimo 9 caratteri.
Oltre a questo, tutti i server devono inviare le seguenti informazioni sui client:
- nome del host dal quale l'utente si sta connettendo
- l'username del client di quel host
- il server sul quale il client è connesso
# 1.2.1 Operators
Ad una classe speciale di client è concesso un ruolo di mantenimento sul network, come:
- disconnettere e riconnettere servers
- rimuovere users
# 1.3 channels
è un gruppo di uno o più clients i quali tutti ricevono messaggi su quel channel.
Si crea implicitamente quando il primo client ci entra. Durante la sua esistenza tutti i client possono riferirsi al channel grazie al suo nome.
## composizione
I nome dei channel sono stringhe, le quali iniziano con `&` o con `#`, con lunghezza fino a 200 caratteri.
Le uniche restrizioni sono:
- non possono contenere spazzi
- un control G `^G` o in ASCII `7`
- una virgola `,`, la quale è usata per una lista
## tipi di channels
Esistono due tipi di channel:
1. channel distribuiti, i quali sono conosciuti da tutti i server che sono connessi al network. I loro nomi iniziano con `#`
2. channel locali, i quali esistono solo sul server su cui è stato creato. I loro nomi iniziano con `&`
Per creare un nuovo channel, o diventare parte di uno già esistente, è richiesto il JOIN nel canale.
- se il canale non esiste, il primo membro ad entrarci sarà l'operatore del canale.
- Se puoi no unirti al canale dipenderà interamente dal tipo di canale, ad esempio `i+` significa invite only.
## se i canali diventano disgiunti
Se per un errore di internet i canali si dovessero separare, allora gli utenti saranno divisi nei canali; e quando ritornerà la connessione tra i due canali, verranno riuniti per poi essere ricongiunti dopo.
# 1.3.1 channel operators
Conosciuto come `chop` o `chanop` su un canale dato è considerato colui che detiene il canale; il quale ha tutti privilegi, come:
- `KICK`
- `MODR`
- `INVITE`
- `TOPIC`
il channel operator è definito dal simbolo `@` dopo il suo nickname