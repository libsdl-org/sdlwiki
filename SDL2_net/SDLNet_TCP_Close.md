###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_Close

Close a TCP network socket.

## Header File

Defined in SDL_net.h

## Syntax

```c
void SDLNet_TCP_Close(TCPsocket sock);

```

## Function Parameters

|              |                  |
| ------------ | ---------------- |
| **sock**     | socket to close. |

## Remarks

All TCP sockets (server and non-server) are deinitialized through this
function. Call this once you are done with a socket, and assume the handle
is invalid once you have.

Closing a socket will disconnect any communication and free its resources.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

