###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_Open

Open a UDP network socket.

## Syntax

```c
UDPsocket SDLNet_UDP_Open(Uint16 port);

```

## Function Parameters

|              |                                      |
| ------------ | ------------------------------------ |
| **port**     | the UDP port to bind this socket to. |

## Return Value

Returns a new UDP socket, ready to communicate.

## Remarks

If `port` is non-zero, the UDP socket is bound to a local port.

The `port` should be given in native byte order, but is used internally in
network (big endian) byte order, in addresses, etc. This allows other
systems to send to this socket via a known port.

Note that UDP sockets at the platform layer "bind" to a nework port number,
but SDL_net's UDP sockets also "bind" to a "channel" on top of that, with
[SDLNet_UDP_Bind](SDLNet_UDP_Bind)(). But the term is used for both.

When you are done communicating over the returned socket, you can shut it
down and free its resources with [SDLNet_UDP_Close](SDLNet_UDP_Close)().

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_UDP_Close](SDLNet_UDP_Close)
* [SDLNet_UDP_Bind](SDLNet_UDP_Bind)

----
[CategoryAPI](CategoryAPI)

