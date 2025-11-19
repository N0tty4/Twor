import re

def parser_irc_message(raw_message):
    tags = {}
    

    if raw_message.startswith('@'):
        str_tags, _, message = raw_message.partition(' ')

        tags_list = str_tags[1:].split(';')

        for single_tag in tags_list:
            key, _, value = single_tag.partition('=')
            tags[key] = value

    else:
        message = raw_message

    group_data = re.search(
            r":([^!]+)!([^@]+)@[^ ]+\.tmi\.twitch\.tv\s\w+\s#([A-Za-z0-9_]+)\s:(.+)\r\n",\
            message)

    if not group_data:
        return None

    name, _, channel, text = group_data.groups()

    return {
        'channel': channel,
        'tags': tags,
        'name': name,
        'text': text
    }
