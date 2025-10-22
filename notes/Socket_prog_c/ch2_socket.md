
# sockets:
Un modo per parlare ad altri programmi usando i standard file descriptors Unix.
# File descriptor:
Quando un programma Unix fa qualsiasi tipo di I/O, lo fanno leggendo o scrivendo su un file descriptor. Un ==file descriptor== è semplicemente un ==numero associato ad un file aperto==. Ma il file può essere una connessione network, una FIFO, un pipe, un terminale, una lettura sul disco, o qualsiasi altra cosa.
# Sockets
Però qui sorge il dubbio: dove trovo il file descriptor per la comunicazione network?
Chiami il `socket()` system routine, il quale ti ritorna il socket descriptor, e tu lo usi per comunicarci usando le speciali `send()` e `recv` chiamate socket.
# 2.1 two type of internet sockets
ne esistono di più tipi, ma i principali sono 2 (i Raw sockets sono potenti, bisogna vederli).
## Stream Sockets `SOCK_STREAM`
I Stream Sockets sono degli affidabili 'two-way connected' flussi di comunicazione. Nel senso: Se invii 1, 2 -> riceverai 1, 2 in ordine; e sono senza errori insomma.
### esempi di utilizzo
ad esempio applicazione come telnet o ssh usano stream sockets. Poiché ogni carattere deve arrivare con sicurezza.
Oppure HTTP usa il stream socket per prendere le pagine
### TCP
Gli stream sockets possono ambire a tale accuratezza nella trasmissione dei messaggi grazie al TCP (Transmission Control Protocol) Il quale si assicura che i dati arrivino senza errori. L'hai sentito nominare in TCP/IP, ma IP (Internet Protocol) ha a che vedere con il routing di internet, non ha niente a che vedere con l'integrità dei dati.
## Datagram Sockets `SOCK_DGRAM`
I Datagram Sockets sono anche chiamati "connectionless sockets". Sono inaffidabili, perché forse arrivano, forse non arrivano, forse arrivano ma in ordine sbagliato, ma, se arriva, il dato nel packet sarà senza errori.
### UDP
Loro pure usano l'IP protocol, ma non usano il TCP protocol, ma il UDP (User Datagram Protocol).
Si definiscono "connectionless" perché non devi mantenere alcuna connessione aperta; basta che: 
- costruisci il tuo packet
- ci metti dentro l'IP handler con le informazioni di destinazione
- e lo mandi.
Non c'è bisogno di alcuna connessione (meglio ribadirlo)
### esempi di utilizzo
Lo si utilizza quando sono si può raggiungere un endpoint con TCP oppure quando una perdita qua e là non sono la fine del mondo. Un esempio di applicazioni sono:
`tftp` (trivial transfer protocol, fratellino di `ftp`), `dhcpcd` (DHCP client).
### perché usarlo
semplicemente per la velocità, non hai bisogno di tener traccia di dove va, basta che lo mandi e te ne dimentichi.
# 2.2 low level Nonsense and network theory
Tutto funziona grazie alla ==data encapsulation ==, semplicemente i dati per essere mandati nel Internet devono utilizzare dei protocolli di rete, i quali avvolgono quelli precedenti e li impacchettano:
```
+----------+----+-----+------+------+++++
| Ethernet | IP | UDP | TFTP | Data |||||
+----------+----+-----+------+------+++++
```
Quando un'altro computer riceve il frame, l'hardware spacchetta il Ethernet, il kernel spacchetta IP e UDP, il programma TFTP spacchetta il TFTP header; ed alla fine potrai leggere il tuo messaggio.
### Layered Network Model (ISO/OSI)
Ha molti vantaggi questo modelli di network, innanzitutto puoi permetterti di pensare solo ai layer che ti interessano, e considerare quelli sotto come perfettamente funzionanti. Il modello si presenta come:
- Application
- presentation
- Session
- Transport
- Network
- Data link
- physical 
### TCP/IP
Ma ai giorni d'oggi di usa un'altro protocollo, che si riduce a 4 layers:
- Application (telnet, FTP, HTTP, etc..)
- Transport (TCP, UDP)
- Internet (IP and routing)
- Data link (Ethernet, WiFi, etc...)
Tutto quello che devi fare per inviare i socket è `send()` i dati. Il kernel costruisce il Transport layer e il Internet Layer per te e l'hardware fa il Network access layer.