###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_OpenClient

Open a client TCP network socket.

## Syntax

```c
TCPsocket SDLNet_TCP_OpenClient(IPaddress *ip);

```

## Function Parameters

|            |                                      |
| ---------- | ------------------------------------ |
| **ip**     | The address to open a connection to. |

## Return Value

Returns the newly created socket, or NULL if there was an error.

## Remarks

Attempt a TCP connection to the remote host and port. The address passed in
should already be swapped to network byte order (addresses returned from
[SDLNet_ResolveHost](SDLNet_ResolveHost.md)() are already in the correct
form).

## Version

This function is available since SDL_net 2.4.0.

## Related Functions

* [SDLNet_TCP_Close](SDLNet_TCP_Close.md)
* [SDLNet_TCP_OpenServer](SDLNet_TCP_OpenServer.md)
* [SDLNet_TCP_Open](SDLNet_TCP_Open.md)

----
[CategoryAPI](CategoryAPI.md)
