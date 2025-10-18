The protocol is for use both with:
- server to server connections
- client to server connections
are more restriction on client connections than server connections.
# 2.2 character codes
No specific character set is specified. The protocol is based on a set of code which are composed of 8 bits, any message may be composed of any number of these octets. Some octet values are used for control codes which act as message delimiter.
Regardless of being an 8-bit protocol, the delimiters and keywords are such that protocol is mostly usable from USASCII terminal and telnet connection.
For his scandinavia origin, the characters `{}|` are considered to be the lower case equivalents of the characters `[]\`.
It is a issue when determining the equivalence of two nicknames.
# 2.3 messages
Server and clients send each other messages which may or may not generate a reply.
If message contains a valid command, the client should expect a reply as specified but it is not advised to wait forever for the reply.
Client-server server-server communication is essentially asynchronous is nature.
## structure of the message
Each IRC message may consist of up to three main parts:
- prefix (optional)
- command
- command parameters (of which there may be up to 15)
these three parts are separated by one or more ASCII space character (`0x20`).
Presence of a prefix is indicated with a single leading ASCII character `: (0x3b)`
- Must be the first character of the message itself.
- Must be no space between the `:` and the prefix.
## prefix in the message
- if the message do not have a prefix, then we assume that is originated from the connection from which arrived.
- Clients should not sue a prefix when they inviate a message for themselves; if the use a prefix, the only one valid is their nickname.
- if the prefix indicate an origin that:
	- isn't in the database
	- the source is registered rom a different link than from which the message arrived, the server must ignore the message silently.
## command format
must wither be:
- valid IRC command 
- or a three digit number represented in ASCII text.
## length and format of message IRC
- each IRC message is a line text that ends with `\r\n (CR-LF)`
- max length is 512 characters, including `\r\n`
	- it means that only 510 character are used for commands + parameters
- not allowed continue a message on more lines
# 2.3 format in pseudo BNF
in computer science, Backus-Naur form (__BNF__), also known as Backus normal form, is a notation system for defining the syntax of programming languages and other formal languages.

The protocol message must be extracted from the contiguous stream of octets. The current solution is to designate two characters, `CR LF`, as message separators. Empty messages are silently ignored, which permits use of the sequence `CR-LF` between messages without extra problems.
The extracted message is parsed into the components:
- \<prefix\>
- \<command\>
- list parameters matched either by \<middle\> or \<trailing\> components
```json
<message>  ::= [':' <prefix> <SPACE> ] <command> <params> <crlf>
<prefix>   ::= <servername> | <nick> [ '!' <user> ] [ '@' <host> ]
<command>  ::= <letter> { <letter> } | <number> <number> <number>
<SPACE>    ::= ' ' { ' ' }
<params>   ::= <SPACE> [ ':' <trailing> | <middle> <params> ]

<middle>   ::= <Any *non-empty* sequence of octets not including SPACE
               or NUL or CR or LF, the first of which may not be ':'>
<trailing> ::= <Any, possibly *empty*, sequence of octets not including
                 NUL or CR or LF>

<crlf>     ::= CR LF
```
# 2.4 numeric replies
Most of the messages sent to the server generate a reply of some sort. The most common reply is the numeric reply (errors and reply).
Numeri reply must be sent as on message consisting of:
- the sender prefix
- three digit numeric
- target of the reply
Numeric reply is not allowed to originate from a client; any such message received by a server are silently dropped. Only the server can inviate numeric reply.
```json
<prefix server> <codice> <destinatario> <testo>
```