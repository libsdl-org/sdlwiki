###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_GetPeerAddress

Get the IP address of the remote system for a socket and channel.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
IPaddress * SDLNet_UDP_GetPeerAddress(UDPsocket sock, int channel);
```

## Function Parameters

|           |             |                                                       |
| --------- | ----------- | ----------------------------------------------------- |
| UDPsocket | **sock**    | the UDP socket to unbind addresses from a channel on. |
| int       | **channel** | the channel of the socket to unbind.                  |

## Return Value

(IPaddress *) Returns the address bound to the socket's channel, or.

## Remarks

If `channel` is -1, then the primary IP port of the UDP socket is returned
-- this is only meaningful for sockets opened with a specific port.

If the channel is not bound and not -1, this function returns NULL.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

