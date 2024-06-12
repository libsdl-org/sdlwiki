###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AddSocket

Add a socket to a socket set, to be checked for available data.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
int SDLNet_AddSocket(SDLNet_SocketSet set, SDLNet_GenericSocket sock);
```

## Function Parameters

|                                              |          |                                        |
| -------------------------------------------- | -------- | -------------------------------------- |
| [SDLNet_SocketSet](SDLNet_SocketSet)         | **set**  | the socket set to add a new socket to. |
| [SDLNet_GenericSocket](SDLNet_GenericSocket) | **sock** | the socket to add to the set.          |

## Return Value

(int) Returns the total number of sockets contained in the set (including
this new one), or -1 if the set is already full.

## Remarks

Generally you don't want to call this generic function, but rather the
specific, inline function that wraps it:
[SDLNet_TCP_AddSocket](SDLNet_TCP_AddSocket)() or
[SDLNet_UDP_AddSocket](SDLNet_UDP_AddSocket)().

This function will fail if you add a socket to the set when the set already
has its maximum number of sockets added, but otherwise it will always
succeed.

If `sock` is NULL, nothing is added to the set; this lets you query the
number of sockets currently contained in the set.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_TCP_AddSocket](SDLNet_TCP_AddSocket)
- [SDLNet_UDP_AddSocket](SDLNet_UDP_AddSocket)
- [SDLNet_DelSocket](SDLNet_DelSocket)
- [SDLNet_TCP_DelSocket](SDLNet_TCP_DelSocket)
- [SDLNet_UDP_DelSocket](SDLNet_UDP_DelSocket)
- [SDLNet_CheckSockets](SDLNet_CheckSockets)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

