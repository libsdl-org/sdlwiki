###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_GetPeerAddress

Get the IP address of the remote system associated with the socket.

## Syntax

```c
IPaddress * SDLNet_TCP_GetPeerAddress(TCPsocket sock);

```

## Function Parameters

|              |                      |
| ------------ | -------------------- |
| **sock**     | the socket to query. |

## Return Value

Returns the address information for the socket.

## Remarks

If the socket is a server socket, this function returns NULL.

This returns a pointer to internal memory; you should not modify or free
it, and should assume it's only valid until the socket is given to
[SDLNet_TCP_Close](SDLNet_TCP_Close).

## Version

This function is available since SDL_net 2.0.0.

----
[CategoryAPI](CategoryAPI)

