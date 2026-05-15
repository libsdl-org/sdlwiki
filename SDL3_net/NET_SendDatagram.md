###### (This function is part of SDL_net, a separate library from SDL.)
# NET_SendDatagram

Send a new packet over a datagram socket to a remote system.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
bool NET_SendDatagram(NET_DatagramSocket *sock, NET_Address *address, Uint16 port, const void *buf, int buflen);
```

## Function Parameters

|                                            |             |                                                                          |
| ------------------------------------------ | ----------- | ------------------------------------------------------------------------ |
| [NET_DatagramSocket](NET_DatagramSocket) * | **sock**    | the datagram socket to send data through.                                |
| [NET_Address](NET_Address) *               | **address** | the [NET_Address](NET_Address) object address. May be NULL to broadcast. |
| Uint16                                     | **port**    | the address port.                                                        |
| const void *                               | **buf**     | a pointer to the data to send as a single packet.                        |
| int                                        | **buflen**  | the size of the data to send, in bytes.                                  |

## Return Value

(bool) Returns true if data sent or queued for transmission, false on
failure; call SDL_GetError() for details.

## Remarks

Datagram sockets send packets of data. They either arrive as complete
packets or they don't arrive at all, as opposed to stream sockets, where
individual bytes might trickle in as they attempt to reliably deliver a
stream of data.

Datagram packets might arrive in a different order than you sent them, or
they may just be lost while travelling across the network. You have to plan
for this. As an added confusion, since SDL_net might send the same packet
on multiple interfaces, you might get duplicate packets, possibly from
different network addresses. You have to plan for this, too.

You can send to any address and port on the network, but there has to be a
datagram socket waiting for the data on the other side for the packet not
to be lost.

General wisdom is that you shouldn't send a packet larger than 1500 bytes
over the Internet, as bad routers might fragment or lose larger ones, but
this limit is not hardcoded into SDL_net and in good conditions you might
be able to send significantly more.

This call never blocks; if it can't send the data immediately, the library
will queue it for later transmission. There is no query to see what is
still queued, as datagram transmission is unreliable, so you should never
assume anything about queued data.

If there's a fatal error, this function will return false. Datagram sockets
generally won't report failures, because there is no state like a
"connection" to fail at this level, but may report failure for
unrecoverable system-level conditions; once a datagram socket fails, you
should assume it is no longer usable and should destroy it with
SDL_DestroyDatagramSocket().

Sending to a NULL address is treated as a request to broadcast a packet.
Note that this will report failure immediately if the socket was not
created with broadcast permission. Broadcast packets are (more or less)
sent to every machine on the LAN, unconditionally.

**WARNING**: It is possible to build a game where everyone is playing on
the same LAN, and every player is simply broadcasting packets. This is
absolutely the wrong thing to do, however. Broadcast packets go to every
device on the LAN, whether they want them or not. The game DOOM, in its
heyday, was capable of
[bringing entire networks to their knees](https://doomwiki.org/wiki/Doom_in_workplaces)
, as many players on the same network would all be broadcasting
relentlessly.

In practice, broadcasting sparingly can be useful for certain
functionality: a LAN-only client broadcasting a few packets to ask for
available servers, and running servers replying directly to that client
without broadcasting at all, is reasonable and safe. Once clients and
servers have found each other, they can communicate directly without any
broadcasting at all. For peer-to-peer games, once connection is
established, it's better to either send unique packets to each known
player, or use a multicasting (which works like broadcast, but only routes
packets to devices that are explicitly listening for it).

With IPv6, which doesn't support broadcasts, broadcasting is faked with
multicast to the all-nodes link-local multicast group, ff02::1, either on a
specific interface or letting the OS choose the default. Other protocols
might fake broadcast operations in similar ways in the future.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_ReceiveDatagram](NET_ReceiveDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

