import irc_client as ircl
import sys
import os
import json
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pypass

def parse_irc_message(raw_message):
    """Estrae i tag, username e testo da un messaggio IRC Twitch."""
    tags = {}
    message_text = ""
    username = ""

    if raw_message.startswith('@'):
        tags_part, _, rest = raw_message.partition(' ')
        for tag in tags_part[1:].split(';'):
            key, _, value = tag.partition('=')
            tags[key] = value
        raw_message = rest

    match = re.match(r":(\w+)!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #[\w]+ :(.+)",\
            raw_message)
    if match:
        username, message_text = match.groups()

    return {
        "username": username,
        "message": message_text,
        "tags": tags,
        "raw": raw_message
    }

if __name__ == '__main__':
    channel = '#martinciriook'


    new_client = ircl.Irc_Client(pypass.token, pypass.nick, channel)
    new_client.connect('+n')

    while True:
        response = new_client.return_data()
        with open('file.jsonl', 'a', encoding='utf-8') as file:
            file.write(json.dumps(parse_irc_message(response))+'\n')

        print(f'{parse_irc_message(response)}\n---------')
