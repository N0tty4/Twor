import sys
import os
import socket

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pypass
if __name__ == '__main__':
    channel = '#stableronaldo'

    # creazione del socket
    sock = socket.socket()
    sock.connect((pypass.server, pypass.port))


    sock.send(f"PASS {pypass.token}\n".encode('utf-8'))
    sock.send(f"NICK {pypass.nick}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))


    while True:
        # sock.recv[n] recive n bytes of data before
        # start processing them.
        # .endcode is used for translate from string to
        # utf-8 encoding.
        response = sock.recv(2048).decode('utf-8')
        print(response)

        
        if response.startswith("PING"):
            sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
