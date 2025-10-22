this section is devoted to describing the actual concepts behind the organization of the IRC protocol.
# 3.1 One-to-one communication
is usually only performed by clients, since most server-server traffic is not a result of servers talking only to each other. It means that servers do not communicate between them, they only inviate the message.
To provide a secure means for clients to talk each other, is required:
- all servers be able to send a message in exactly one direction along the ==spanning tree==
- path of message being delivered is the shortest path between any two points on the spanning tree
# 3.2 one-to-many
Main goal of IRC provide a forum which allows efficient conferencing (one to many conversations). IRC offers several means to achieve this, each serving its own purpose.
### to a list
least efficient style of one-to-many conversation is through clients talking to a list of users.
1. The client gives a list of destination to which the message is to be delivered and the server breaks it up and dispatches a separate copy of the message to each given destination.
2. Isn't as efficient as using a group since the destination list is broken up and the dispatch sent without checking to make sure duplicates aren't sent down each path.
### to a group (channel)
In IRC the channel has a role equivalent to that of the multicast group; their existence is dynamic (coming and going as people join and leave channels).
The actual conversation is only sent to server which are supporting users on a given channel.
If there are multiple users on a server in the same channel, the message text is sent only once to that server and then sent to each client on the channel.
This action is repeated for each client-server combination until finish.
