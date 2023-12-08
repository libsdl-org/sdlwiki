###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreeSocketSet

Free a set of sockets allocated by [SDLNet_AllocSocketSet](SDLNet_AllocSocketSet.md)().

## Syntax

```c
void SDLNet_FreeSocketSet(SDLNet_SocketSet set);

```

## Function Parameters

|             |                         |
| ----------- | ----------------------- |
| **set**     | the socket set to free. |

## Remarks

When done with a socket set, call this function to free its resources.

This only frees the socket set, not the individual sockets in the set,
which would still (at some future point) need to be closed with
[SDLNet_TCP_Close](SDLNet_TCP_Close.md) or
[SDLNet_UDP_Close](SDLNet_UDP_Close.md).

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
