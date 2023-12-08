###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_OpenServer

Open a server TCP network socket.

## Syntax

```c
TCPsocket SDLNet_TCP_OpenServer(IPaddress *ip);

```

## Function Parameters

|            |                                  |
| ---------- | -------------------------------- |
| **ip**     | The address to host a server on. |

## Return Value

Returns the newly created socket, or NULL if there was an error.

## Remarks

If `ip->host` is INADDR_NONE or INADDR_ANY, the socket is bound to all
interfaces, otherwise it is bound to the specified interface. The address
passed in should already be swapped to network byte order (addresses
returned from [SDLNet_ResolveHost](SDLNet_ResolveHost.md)() are already in the
correct form).

## Version

This function is available since SDL_net 2.4.0.

## Related Functions

* [SDLNet_TCP_Close](SDLNet_TCP_Close.md)
* [SDLNet_TCP_OpenClient](SDLNet_TCP_OpenClient.md)
* [SDLNet_TCP_Open](SDLNet_TCP_Open.md)

----
[CategoryAPI](CategoryAPI.md)
