###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_Recv

Receive data from a non-server socket.

## Header File

Defined in SDL_net.h

## Syntax

```c
int SDLNet_TCP_Recv(TCPsocket sock, void *data, int maxlen);

```

## Function Parameters

|                |                                                           |
| -------------- | --------------------------------------------------------- |
| **sock**       | the socket to send data to.                               |
| **data**       | a pointer to where to store received data.                |
| **maxlen**     | the maximum number of bytes that can be stored at `data`. |

## Return Value

Returns number of bytes received, which might be less than `maxlen`.

## Remarks

`sock` must be a valid socket that was created by
[SDLNet_TCP_Open](SDLNet_TCP_Open) with a specific address, or
[SDLNet_TCP_Accept](SDLNet_TCP_Accept).

Receive up to `maxlen` bytes of data over the non-server socket `sock`, and
store them in the buffer pointed to by `data`.

This function returns the actual amount of data received. If the return
value is less than or equal to zero, then either the remote connection was
closed, or an unknown socket error occurred.

Note that this will return the number of bytes available at the first
moment the socket is able to see new data. If packets are coming in slowly
from the network, this might be less data than you expect at a given time.

This function may block! Use [SDLNet_CheckSockets](SDLNet_CheckSockets)()
to make sure there is data available before calling this function, if you
want to avoid blocking.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_TCP_Send](SDLNet_TCP_Send)
- [SDLNet_CheckSockets](SDLNet_CheckSockets)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

