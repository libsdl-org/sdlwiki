###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AddSocket

Add a socket to a socket set, to be checked for available data.

## Syntax

```c
int SDLNet_AddSocket(SDLNet_SocketSet set, SDLNet_GenericSocket sock);

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

Generally you don't want to call this generic function, but rather the
specific, inline function that wraps it:
[SDLNet_TCP_AddSocket](SDLNet_TCP_AddSocket.md)() or
[SDLNet_UDP_AddSocket](SDLNet_UDP_AddSocket.md)().

This function will fail if you add a socket to the set when the set already
has its maximum number of sockets added, but otherwise it will always
succeed.

If `sock` is NULL, nothing is added to the set; this lets you query the
number of sockets currently contained in the set.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_TCP_AddSocket](SDLNet_TCP_AddSocket.md)
* [SDLNet_UDP_AddSocket](SDLNet_UDP_AddSocket.md)
* [SDLNet_DelSocket](SDLNet_DelSocket.md)
* [SDLNet_TCP_DelSocket](SDLNet_TCP_DelSocket.md)
* [SDLNet_UDP_DelSocket](SDLNet_UDP_DelSocket.md)
* [SDLNet_CheckSockets](SDLNet_CheckSockets.md)

----
[CategoryAPI](CategoryAPI.md)
