###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_UDP_Close

Close a UDP socket.

## Header File

Defined in SDL_net.h

## Syntax

```c
void SDLNet_UDP_Close(UDPsocket sock);

```

## Function Parameters

|              |                      |
| ------------ | -------------------- |
| **sock**     | UDP socket to close. |

## Remarks

This disconnects the socket and frees any resources it retains.

This socket may not be used again once given to this function.

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

