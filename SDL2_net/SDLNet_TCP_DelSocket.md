###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_DelSocket

Remove a TCP socket from a socket set.

## Header File

Defined in SDL_net.h

## Syntax

```c
SDL_FORCE_INLINE int SDLNet_TCP_DelSocket(SDLNet_SocketSet set, TCPsocket sock);
```

## Function Parameters

|              |                                         |
| ------------ | --------------------------------------- |
| **set**      | the socket set to remove a socket from. |
| **sock**     | the socket to remove from the set.      |

## Return Value

Returns the total number of sockets contained in the set (after `sock`'s
removal), or -1 if `sock` was not in the set.

## Remarks

This is a small TCP-specific wrapper over
[SDLNet_DelSocket](SDLNet_DelSocket); please refer to that function's
documentation.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_DelSocket](SDLNet_DelSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

