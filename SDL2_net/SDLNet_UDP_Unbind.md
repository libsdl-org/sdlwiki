###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_Unbind

Unbind all addresses from the given channel.

## Syntax

```c
void SDLNet_UDP_Unbind(UDPsocket sock, int channel);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **sock**        | the UDP socket to unbind addresses from a channel on. |
| **channel**     | the channel of the socket to unbind.                  |

## Remarks

Note that UDP sockets at the platform layer "bind" to a nework port number,
but SDL_net's UDP sockets also "bind" to a "channel" on top of that, with
[SDLNet_UDP_Bind](SDLNet_UDP_Bind.md)(). But the term is used for both.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_UDP_Bind](SDLNet_UDP_Bind.md)

----
[CategoryAPI](CategoryAPI.md)
