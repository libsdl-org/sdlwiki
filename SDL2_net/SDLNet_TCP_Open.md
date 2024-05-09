###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_Open

Open a TCP network socket.

## Header File

Defined in SDL_net.h

## Syntax

```c
TCPsocket SDLNet_TCP_Open(IPaddress *ip);

```

## Function Parameters

|            |                                                               |
| ---------- | ------------------------------------------------------------- |
| **ip**     | The address to open a connection to (or to host a server on). |

## Return Value

Returns the newly created socket, or NULL if there was an error.

## Remarks

If `ip->host` is INADDR_NONE or INADDR_ANY, this creates a local server
socket on the given port, otherwise a TCP connection to the remote host and
port is attempted. The address passed in should already be swapped to
network byte order (addresses returned from
[SDLNet_ResolveHost](SDLNet_ResolveHost)() are already in the correct
form).

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_TCP_Close](SDLNet_TCP_Close)
- [SDLNet_TCP_OpenServer](SDLNet_TCP_OpenServer)
- [SDLNet_TCP_OpenClient](SDLNet_TCP_OpenClient)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

