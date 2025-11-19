#!/usr/bin/env python3

# irc_connections
import irc_client as ircl

#parsing
import cmd
import argparse
from parsers import parser_irc as prsirc
from parsers import comand_parser as cmdprs

# files
import yaml
import json
import pypass

# initial parser for defined configuration
parser = argparse.ArgumentParser(
        prog='Twor',
        description='display, store for usage twitch\' chats',
        epilog='fish of documentation')
parser.add_argument('--config')
args = parser.parse_args()

print("\x1b[2J\x1b[0;0H", end='')

# start of our cli command
class CmdTwor(cmd.Cmd):
    # create istance of our irc client
    client = ircl.Irc_Client(pypass.nick, pypass.client_id, pypass.passwd, pypass.helix_passwd)
    prompt = 'not connected> '

    channel = None
    mode_msg = ''

    def do_connect(self, arg):
        args = cmdprs.parse_command_args(arg)

        if len(args['args']) == 0:
            print("insert the name of a channel and the modality")
            return None

        self.channel = args['args']
        self.prompt = f'connected on \x1b[31m{self.channel}\x1b[0m> '
        self.client = ircl.Irc_Client(pypass.nick, pypass.client_id, pypass.passwd, pyapass.helix_passwd, self.channel)


        if len(args['opts']['-m']) >= 0:
            self.mode_msg = args['opts']['-m']
            print(self.mode_msg)

        try:
            self.client.connect(f'CAP REQ :{self.mode_msg}\n')
            if self.mode_msg:
                print(f"connected to {self.channel} with modality {self.mode_msg}")
            else:
                print(f"connected to {self.channel} with no special modality")

        except Exception as e:
            print("errore connessione", e)

    def do_leave(self, arg):
        if not arg:
            command = f'PART #{self.channel}\n'
        else:
            command = f'PART #{arg}\n'

        returned_len = self.client.send_after_connect(command)
        self.channel = 'not_connected> '

        if returned_len != len(command):
            print(f"error sending message:\n{returned_len}\n{len(command)}")
        else:
            self.channel = None
            self.prompt = f'not connected> '
            self.mode_msg = ''

    def do_data_out(self, arg):
        args = arg.split()

        if len(args) == 1:
            file_path = args[0]
            response = ''
            print_chat = True

            while print_chat:
                try:
                    response = self.client.return_data()
                    with open(file_path, 'a') as FILE:
                            FILE.write(\
                                json.dumps(prsirc.parser_irc_message(response),\
                                indent = 4))

                except KeyboardInterrupt:
                    print_chat = False
                    print('\x1b[2K\r')

        else:
            response = ''
            print_chat = True
            while print_chat:
                try:
                    response = self.client.return_data()
                    print(f'\n\n\n------- \n{response}--------\n\n\n')
                    print(json.dumps(prsirc.parser_irc_message(response)))

                except KeyboardInterrupt:
                    print_chat = False
                    print('\x1b[2K\r')

    def do_print_top_streamers(self, arg):
        top_streamers = self.client.live_channels(arg)
        for dicts in top_streamers:
            print(dicts['user_name'])

    def do_clear(self, arg):
        print("\x1b[2J\x1b[0;0H", end= '')

    def do_quit(self, arg):
        print("quitting...")
        return True


if __name__ == '__main__':
    CmdTwor().cmdloop()

# in normal modality:
# creare l'istanza con dentro 
#    il nichname, 
#    la password del client irc
#    la password del server helix
