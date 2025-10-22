```python
import sys
import os
import socket

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pypass
if __name__ == '__main__':
    channel = '#mokrivskyi'

    # creazione del socket
    sock = socket.socket()
    sock.connect((pypass.server, pypass.port))


    sock.send(f"PASS {pypass.token}\n".encode('utf-8'))
    sock.send(f"NICK {pypass.nick}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))


    while True:
        response = sock.recv(2048).decode('utf-8')
        print(response)

        if response.startswith("PING"):
            sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))

```
# socket
Un socket in python è un endpoint che server per inviare e ricevere dati nell'internet usando le API socket.
# recv()
Viene usato per ricevere i dati attraverso un network socket.
## concetti fondamentali
La funzione `recv` è usata per ricevere i dati da un socket connesso.
I dati ricevuti sono bufferizzati nello stack di network prima di essere passati alla chiamata `recv`.
## sintassi di base
```python
import socket
socket.recv(bufsize[, flags])
```
- `bufsize` è l'inter che specifica il massimo numero di dati che si riceve prima di processare i dati
- `falgs` è un parametro opzionale che può essere usato per modificare il comportamento di `recv`.
