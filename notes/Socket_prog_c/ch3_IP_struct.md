# 3.1 IP Addresses, version 4 and 6
Il Internet Protocol Version 4 (IPv4) è formato da 4 bytes (4 ottetti) ed era solitamente scritto con numeri e punti `192.0.2.111`. Il problema stava nel fatto che solamente $2^{32}$ possibili indirizzi potevano essere usati, quindi è stato creato il Internet Protocol Version 6 (IPv6), che può avere fino a $2^{128}$ indirizzi.
## 3.1.1 Sub-nets
Per ragioni di organizzazione è comodo dire ad esempio che "questa parte di indirizzo IP è la porzione per il ==network==, e l'altra parte è la ==porzione per il host==".
Ad esempio, puoi avere `192.0.2.12` e noi possiamo dire che i primi 3 byte sono per il network e l'ultimo è per l'host. In passato c'erano le cassi di network.
### net-mask
La porzione di network dell'indirizzo IP è descritta dal ==net-mask==, con il quale fail il bit-wise-AND con l'indirizzo IP per avere il numero del network.
Ad esempio solitamente è come `255.255.255.0`. Però non sempre le persone sanno idea di quanti bits sono, e non è molto compatto.
Quindi, nel nuovo stile, semplicemente metti uno slash dopo l'indirizzo IP per indicare il numero di network bits in decimale. Come `192.0.2.12/30`.
## 3.1.2 port Number
Oltre all'indirizzo IP, c'è anche un altro indirizzo usato dal TCP e UDP; ed è il numero di porta. è un numero a 16 bit che è come l'indirizzo locale per la connessione.
Per immaginartelo meglio, pensa all'indirizzo IP come alla via di un hotel; e al ==port number== come alla stanza specifica del hotel.
### esempio di implementazione
Diciamo che vuoi un computer che possa gestire le mail che arrivano e i servizi web; come potresti fare per differenziarli con un unico indirizzi IP? Semplice, differenti servizi hanno differenti porte. Ad esempio nei sistemi operativi Unix sono in `/etc/services`. Le porte sotto 1024 sono considerate speciali; solitamente richiedono privilegi speciali.
# 3.2 byte order
Esistono due tipi di ordinamento nell'internet. Innanzitutto bisogna specificare che se su internet vuoi rappresentare ad esempio `b34f`, lo memorizzerai come 2 bytes sequenziali `b3` e `4f`. Questo si chiama Big-Endian notation.
Mentre l'altro modo è attraverso il Little-Endian, il quale memorizza `b34f` come prima `4f` e poi `b3`.
il ==Big-Endian== è chiamato anche ==Network-Byte==, il motivo si può immaginare (si usa su internet).
Il tuo computer memorizza i numeri in ==Host Byte Order==; quindi devi essere sicuro che il messaggio sia tradotto nel linguaggio di internet.
Si assume che sempre il tuo ordinamento si sbagliato e si chiama una funzione che in qualunque caso vada a tradurre il tuo ordinamento:

| function  | Description           |
| --------- | --------------------- |
| `htons()` | Host TO Network Short |
| `htonl()` | Host TO Network Long  |
| `ntohs()` | Network TO Host Short |
| `ntohl()` | Network TO Host Long  |
Dove short è per 2 byte e long è per 4 byte.
# 3.3 structs
## socket descriptor
è solamente un `int`, il quale come detto prima rappresenta un numero associato ad un file aperto.
## `struct addrinfo`
è usato per preparare il ==socket address struct== per poi usarlo. Viene anche usato nel ==host name lookups== e ==service name lookup==. Per il momento ricordati solo che è la prima cosa che chiami per creare una connessione.
```c
struct addrinfo {
int ai_flags;             // AI_PASSIVE, AI_CANONNAME, etc.
int ai_family;            // AF_INET, AF_INET6, AF_UNSPEC
int ai_socktype;          // SOCK_STREAM, SOCK_DGRAM
int ai_protocol;          // use 0 for "any"
size_t ai_addrlen;        // size of ai_addr in bytes
struct sockaddr *ai_addr; // struct sockaddr_in or _in6
char *ai_canonname;       // full canonical hostname

struct addrinfo *ai_next; // linked list, next node

};
```
Puoi riempire questa struttura e poi chiamare `getaddrinfo()`; il quale ritornerà un puntatore alla nuova linked list riempita con quello che vuoi.
- Puoi obbligarlo ad usare IPv4 o IPv6 nel parametro `ai_family`, oppure mettere semplicemente `AF_UNSPEC` per far fare  tutto al programma.
- `ai_next` punta al prossimo nodo nella lista.
- `ai_addr` è un puntatore a `struct sockaddr` (IP address struct)
Non sempre avrai bisogno di riempire da solo tutta la struct, infatti spesso si usa la chiamata a `getaddrinfo()` per riempire `struct addrinfo`.
Però dovrai scavare nella struttura per accedere alle sotto-strutture.
### `struct sockaddr`
Contiene le informazioni degli indirizzi di molti tipi di socket
```c
struct sockaddr {
unsigned short sa_family;           // address family, AF_xxx
char           sa_data[14];         // 14 bytes of protocol address
};
```
- `sa_family` può essere una varietà di cose, ma sara di due tipi:
	- `AF_INET` (IPv4)
	- `AF_INET6` (IPv6)
- `sa_data` contiene l'indirizzo di destinazione e il `port number` 
### `struct sockaddr_in` 
Per averci a che fare con `struct sockaddr` si è creata una struttura parallela; in questo caso `_in` sta per Internet; da essere usato con IPv4.
Importante, un puntatore a `struct sockaddr_in` può essere castato ad un puntatore `struct sockaddr` e vice-versa.
```c
struct sockaddr_in {
short int          sin_family;  // Address family, AF_INET
unsigned short int sin_port;    // Port number
struct in_addr     sin_addr;    // Internet address
unsigned char      sin_zero[8]; // Same size as struct sockaddr
};
```
Questa struttura rende più facile riferirci agli elementi del `socket address`.
- `sin_zero[8]` è incluso come padding per renderla uguale a `struct sockaddr`
- `sin_family` corrisponde ad `sa_family`; e dovrebbe essere settato a `AF_INET`
- `sin_port` deve essere in ==Network Byte Order== (`htons()`)
- `sin_addr` è una struttura `in_addr`
### `in_addr`
```c
// (IPv4 only--see struct in6_addr for IPv6)
// Internet address (a structure for historical reasons)
struct in_addr {
uint32_t s_addr; // that's a 32-bit int (4 bytes)
};
```
## IPv6 structs
```c
// (IPv6 only--see struct sockaddr_in and struct in_addr for IPv4)
struct sockaddr_in6 {
	u_int16_t sin6_family;     // address family, AF_INET6
	u_int16_t sin6_port;       // port, Network Byte Order
	u_int32_t sin6_flowinfo;   // IPv6 flow information
	struct in6_addr sin6_addr; // IPv6 address
	u_int32_t sin6_scope_id;   // Scope ID
};
struct in6_addr {
unsigned char s6_addr[16];     //IPv6 address
};
```
### `struct sockaddr_storage`
è stata progettata per essere abbastanza grande da contenere IPv4 e IPv6 structures.
```c
struct sockaddr_storage {
sa_family_t ss_family; // address family
// all this is padding, implementation specific, ignore it:
char        __ss_pad1[_SS_PAD1SIZE];
int64_t     __ss_align;
char        __ss_pad2[_SS_PAD2SIZE];
};
```
# 3.4 IP address, part deux