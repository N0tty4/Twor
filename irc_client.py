import socket
import pypass
import requests

class Irc_Client:

    def __init__(self, nick, client_id, passwd, helix_passwd,\
            host='irc.chat.twitch.tv', port=6667):

        self.nick = nick
        self.client_id = client_id

        self.passwd = passwd
        self.helix_passwd = helix_passwd

        self.channel = ''

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

        self.base_url = 'https://api.twitch.tv/helix'

        self.headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.helix_passwd}'
        }

    def connect(self, args):

        self.sock.connect((self.host, self.port))
        self.sock.send(f"PASS oauth:{self.passwd}\r\n".encode('utf-8'))
        self.sock.send(f"NICK {self.nick}\r\n".encode('utf-8'))
        self.sock.send(f"{args}\r\n".encode('utf-8'))
        self.sock.send(f"JOIN #{self.channel}\r\n".encode('utf-8'))

    def send_after_connect(self, arg):
        return self.sock.send(f'{arg}'.encode('utf-8'))

    #da sistemare
    def return_data(self):
        data = self.sock.recv(2048).decode('utf-8')

        if data.startswith('PING'):
            return 'PONG :tmi.twitch.tv\r\n'

        return data

    def live_channels(self, n):
        if n != '':
            params = {"first": n}

        else:
            params = {"first": 5}

        url = f"{self.base_url}/streams"
        response = requests.get(url, headers=self.headers, params=params)

        print("Status Code:", response.status_code)
        #print("Response:", response.text)

        return response.json().get("data")
