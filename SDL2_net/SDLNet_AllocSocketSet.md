###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AllocSocketSet

Allocate a socket set for use with [SDLNet_CheckSockets](SDLNet_CheckSockets)().

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
SDLNet_SocketSet SDLNet_AllocSocketSet(int maxsockets);
```

## Function Parameters

|     |                |                                                       |
| --- | -------------- | ----------------------------------------------------- |
| int | **maxsockets** | the maximum amount of sockets to include in this set. |

## Return Value

([SDLNet_SocketSet](SDLNet_SocketSet)) Returns a socket set for up to
`maxsockets` sockets, or NULL if the function ran out of memory.

## Remarks

To query if new data is available on a socket, you use a "socket set" with
[SDLNet_CheckSockets](SDLNet_CheckSockets)(). A socket set is just a list
of sockets behind the scenes; you allocate a set and then add/remove
individual sockets to/from the set.

When done with a socket set, you can free it with
[SDLNet_FreeSocketSet](SDLNet_FreeSocketSet).

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_FreeSocketSet](SDLNet_FreeSocketSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

