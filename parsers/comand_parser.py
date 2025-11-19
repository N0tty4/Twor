def conct_mode(mode):

    expanse_mode = []
    if 't' in mode:
        expanse_mode.append('twitch.tv/tags')
    if 'c' in mode:
        expanse_mode.append('twitch.tv/commands')
    if 'm' in mode:
        expanse_mode.append('twitch.tv/membership')
    return ' '.join(expanse_mode)


def parse_command_args(raw_args):
    parsed = {
        'args' : '',
        'opts' : {
            '-m' : [],    
            '-f' : []
        }
    }

    commands = raw_args.split()
    print(commands)
    parsed['args'] = commands[0]
    expanse_mode = []

    actual_opt = ''
    for opt in commands[1:]:
        if opt.startswith('-'):
            actual_opt = opt

        else:
            if actual_opt == '-m' or actual_opt == '--mode':
                actual_opt = '-m'

                parsed['opts'][actual_opt].append(opt)

            if actual_opt == '-f' or actual_opt == '--file':
                actual_opt = '-f'

                parsed['opts'][actual_opt].append(opt)

    for el in parsed['opts']['-m']:

        if el in 'tcm':
            if 't' in el:
                expanse_mode.append('twitch.tv/tags')
            if 'c' in el:
                expanse_mode.append('twitch.tv/commands')
            if 'm' in el:
                expanse_mode.append('twitch.tv/membership')
        else:
            if 'tags' == el:
                expanse_mode.append('twitch.tv/tags')
            if 'commands' == el:
                expanse_mode.append('twitch.tv/commands')
            if 'membership' == el:
                expanse_mode.append('twitch.tv/membership')

    parsed_modes = ' '.join(expanse_mode)
    parsed['opts']['-m'] = parsed_modes

    return parsed

if __name__ == '__main__':

    str_arr = [
        'chat_twitch -m tcm --file file.jsonl',
        'chat_twitch -m tcm -f file.jsonl',
        'chat_twitch --mode tags commets membership',
        'chat_twitch --mode tcm --file file.jsonl',
        'chat_twitch --mode tags comments memebership'
    ]

    for el in str_arr:
        print(type(el))
        print(parse_command_args(el))

# connet <name channel> -m modality -f file.jsonl
#
# parsed = {
#   args = <name channel>
#   opts = {
#       '-m' = [tags, comments, membership]
#       '-f' = 'file.jsonl'
#   }
# }
#
#
#
#
#
