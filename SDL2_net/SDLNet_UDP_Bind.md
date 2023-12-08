###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_Bind

Bind an address to the requested channel on the UDP socket.

## Syntax

```c
int SDLNet_UDP_Bind(UDPsocket sock, int channel, const IPaddress *address);

```

## Function Parameters

|                 |                                                                                 |
| --------------- | ------------------------------------------------------------------------------- |
| **sock**        | the UDP socket to bind an address to a channel on.                              |
| **channel**     | the channel of the socket to bind to, or -1 to use the first available channel. |
| **address**     | the address to bind to the socket's channel.                                    |

## Return Value

Returns the channel which was bound, or -1 on error.

## Remarks

Note that UDP sockets at the platform layer "bind" to a nework port number,
but SDL_net's UDP sockets also "bind" to a "channel" on top of that, with
[SDLNet_UDP_Bind](SDLNet_UDP_Bind.md)(). But the term is used for both.

If `channel` is -1, then the first unbound channel that has not yet been
bound to the maximum number of addresses will be bound with the given
address as it's primary address.

If the channel is already bound, this new address will be added to the list
of valid source addresses for packets arriving on the channel. If the
channel is not already bound, then the address becomes the primary address,
to which all outbound packets on the channel are sent.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_UDP_Unbind](SDLNet_UDP_Unbind.md)

----
[CategoryAPI](CategoryAPI.md)
