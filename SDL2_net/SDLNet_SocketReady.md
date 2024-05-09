###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_SocketReady

See if a specific socket has data available after checking it in a set.

## Header File

Defined in SDL_net.h

## Syntax

```c
#define SDLNet_SocketReady(sock) _SDLNet_SocketReady((SDLNet_GenericSocket)(sock))
```

## Macro Parameters

|              |                      |
| ------------ | -------------------- |
| **sock**     | the socket to check. |

## Return Value

Returns non-zero if socket has new data available, zero otherwise.

## Remarks

After calling [SDLNet_CheckSockets](SDLNet_CheckSockets)(), you can use
this function on a socket that was in the socket set, to find out if data
is available for reading.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

