###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_AddSocket

Add a TCP socket to a socket set, to be checked for available data.

## Header File

Defined in SDL_net.h

## Syntax

```c
SDL_FORCE_INLINE int SDLNet_TCP_AddSocket(SDLNet_SocketSet set, TCPsocket sock);
```

## Function Parameters

|              |                                        |
| ------------ | -------------------------------------- |
| **set**      | the socket set to add a new socket to. |
| **sock**     | the socket to add to the set.          |

## Return Value

Returns the total number of sockets contained in the set (including this
new one), or -1 if the set is already full.

## Remarks

This is a small TCP-specific wrapper over
[SDLNet_AddSocket](SDLNet_AddSocket); please refer to that function's
documentation.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_AddSocket](SDLNet_AddSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

