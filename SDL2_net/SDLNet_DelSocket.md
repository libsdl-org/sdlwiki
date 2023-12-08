###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_DelSocket

Remove a socket from a set of sockets to be checked for available data.

## Syntax

```c
int SDLNet_DelSocket(SDLNet_SocketSet set, SDLNet_GenericSocket sock);

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

Generally you don't want to call this generic function, but rather the
specific, inline function that wraps it:
[SDLNet_TCP_DelSocket](SDLNet_TCP_DelSocket.md)() or
[SDLNet_UDP_DelSocket](SDLNet_UDP_DelSocket.md)().

If `sock` is NULL, nothing is removed from the set; this lets you query the
number of sockets currently contained in the set.

This will return -1 if the socket was not found in the set; in such a case,
nothing is removed from the set.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_TCP_DelSocket](SDLNet_TCP_DelSocket.md)
* [SDLNet_UDP_DelSocket](SDLNet_UDP_DelSocket.md)
* [SDLNet_AddSocket](SDLNet_AddSocket.md)
* [SDLNet_TCP_AddSocket](SDLNet_TCP_AddSocket.md)
* [SDLNet_UDP_AddSocket](SDLNet_UDP_AddSocket.md)
* [SDLNet_CheckSockets](SDLNet_CheckSockets.md)

----
[CategoryAPI](CategoryAPI.md)
