import socket

class Irc_Client:

    def __init__(self, passwd, nick, channel, host='irc.chat.twitch.tv', port=6667):
        self.passwd = passwd
        self.nick = nick
        self.channel = channel

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self, type = 'n'):

        self.sock.connect((self.host, self.port))
        self.sock.send(f"PASS {self.passwd}\n".encode('utf-8'))
        self.sock.send(f"NICK {self.nick}\n".encode('utf-8'))
        
        if type ==  '+n':
            self.sock.send("CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\n".encode('utf-8'))

        self.sock.send(f"JOIN {self.channel}\n".encode('utf-8'))

    # return the data from the API
    def return_data(self):
        while True:
            response = self.sock.recv(2048).decode('utf-8')            

            if response.startswith('PING'):
                self.sock.send('PONG :tmi.twitch.tv\n'.encode('utf-8'))

            return response
