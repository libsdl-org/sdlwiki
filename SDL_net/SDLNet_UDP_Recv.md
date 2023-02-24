====== (This function is part of SDL_net, a separate library from SDL.) ======
= SDLNet_UDP_Recv =

Receive a single packet from a UDP socket.

== Syntax ==

<syntaxhighlight lang='c'>
int SDLNet_UDP_Recv(UDPsocket sock, UDPpacket *packet);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sock'''
|the UDP socket to receive packets on.
|-
|'''packet'''
|a single packet to receive data into from the network.
|}

== Return Value ==

Returns 1 if a new packet is available, or -1 on error. 0 means no packets
were currently available.

== Remarks ==

The returned packets contain the source address and the channel they
arrived on. If they did not arrive on a bound channel, the the channel will
be set to -1.

The channels are checked in highest to lowest order, so if an address is
bound to multiple channels, the highest channel with the source address
bound will be returned.

This function does not block, so it can return 0 packets pending, which is
not an error condition.

== Version ==

This function is available since SDL_net 2.0.0.

== Related Functions ==

:[[SDLNet_UDP_Send]]
:[[SDLNet_UDP_RecvV]]

----
[[CategoryAPI]]


