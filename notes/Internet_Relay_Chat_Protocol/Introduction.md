Was implemented as a means for users on a ==BBS (Bulletin Board System)== to chat among themselves. Is a text-based protocol, whose simplest client is any socket program that can connect to the server.
## basic concept
has developed on systems  using the TCP/IP network protocol. Is a teleconferencing system (through the use of client-server model) runs on many machines in a distributed fashion. 
Typical setup is:
- single process (server) formina a central point
- clients (or other servers) to connect to.
# 1.1 Servers
The server forms the backbone of IRC, providing:
- a point to which clients may connect to talk each other
- point for other servers to connect to -> forming IRC network.
Only network allowed is that of a ==spanning tree==: each server acts as a central node fro the rest of the net.
# 1.2 Clients
A client is anything connecting to a server that is not another server.
Each client is distinguished from another clients by: ==nickname of max 9 characters==.
In addition, to the nickname, all servers must have the following information about all clients:
- real name of the host that the client is running on
- the username of the client on that host
- server to which the client is connected.
# 1.2.1 Operators
Are a special class of clients is allowed to perform general maintenance function on the network.
The powers granted to an operator could be 'dangerous' they are still necessary. Should be able to perform basic network tasks:
- disconnecting and reconnecting servers
- remove a user
# 1.3 Channels
is an named group of one or more clients which will all receive messages addresses to that channel.
Is created implicitly when the first client joins it; while exists, any client can reference the channel using the name of the channel.
## composition
channels names are strings (being with `&` or `#` character) of length up to 200 characters.
The only restrictions is:
- not contain any spaces ' '
- a control G `^ G` ora in ASCII 7
- a comma `,` which is used as a list item separator by the protocol
## type of channels
there are two type of channels:
1. distributed channel, which is known to all the servers that are connected to the network.
   The name starts with `#` character
2. local channel, exists only on the server where was created.
   the name starts with `&`
To create new channel or become parto of an existing channel, a user is required to JOIN to channel.
- If the channel not exists, then the first user that join in will become a channel operator.
- If the channel already exists, whether or not your request to JOIN that channel depends on the current modes of the channel.
  For example, `(+i)` is invite only.
  
If the IRC network becomes disjoint because of a split between two servers, the channel on each side is only composed of those clients which are connect to servers on the respective sides of the split.
## 1.3.1 channel operators
Also referred as "chop" or "chanop" on a given channel, own the channel. In recognition of this status, channel operators are endowed with certain powers which enable the to keep control and some sort of sanity in their channel. These commands are:
- KICK
- MODE
- INVITE
- TOPIC
A channel operator is identified by the `@` symbol next to their nickname whenever it is associated with a channel