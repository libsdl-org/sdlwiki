###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_SendV

Send a vector of packets to the the channels specified within the packet.

## Syntax

```c
int SDLNet_UDP_SendV(UDPsocket sock, UDPpacket **packets, int npackets);

```

## Function Parameters

|                  |                                               |
| ---------------- | --------------------------------------------- |
| **sock**         | the UDP socket to send packets on.            |
| **packets**      | an array of packets to send to the network.   |
| **npackets**     | the number of packets in the `packets` array. |

## Return Value

Returns the number of packets successfully sent from this machine.

## Remarks

If the channel specified in the packet is -1, the packet will be sent to
the address in the `src` member of the packet.

Each packet will be updated with the status of the packet after it has been
sent, -1 if the packet send failed.

This function takes an array of packets but does not need to be allocated
through [SDLNet_AllocPacketV](SDLNet_AllocPacketV.md); if you supply your own
array of packets you allocated individually, that is okay.

**Warning**: UDP is an _unreliable protocol_, which means we can report
that your packet has been successfully sent from your machine, but then it
never makes it to its destination when a router along the way quietly drops
it. If this happens--and this is a common result on the internet!--you will
not know the packet never made it. Also, packets may arrive in a different
order than you sent them. Plan accordingly!

**Warning**: The maximum size of the packet is limited by the MTU (Maximum
Transfer Unit) of the transport medium. It can be as low as 250 bytes for
some PPP links, and as high as 1500 bytes for ethernet. Different sizes can
be sent, but the system might split it into multiple transmission fragments
behind the scenes, that need to be reassembled on the other side (and the
packet is lost if any fragment is lost in transit). So the less you can
reasonably send in a single packet, the better, as it will be more reliable
and lower latency.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_UDP_RecvV](SDLNet_UDP_RecvV.md)

----
[CategoryAPI](CategoryAPI.md)
