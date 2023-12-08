###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_TCP_Send

Send data over a non-server socket.

## Syntax

```c
int SDLNet_TCP_Send(TCPsocket sock, const void *data, int len);

```

## Function Parameters

|              |                                                         |
| ------------ | ------------------------------------------------------- |
| **sock**     | the socket to send data to.                             |
| **data**     | a pointer to the bytes to send.                         |
| **len**      | the number of bytes, pointed to by `data`, to transmit. |

## Return Value

Returns number of bytes sent, which might be less if there was a problem or
connection failure. If the socket is invalid, this function can return -1,
but in valid uses it'll return >= 0.

## Remarks

`sock` must be a valid socket that was created by
[SDLNet_TCP_Open](SDLNet_TCP_Open.md) with a specific address, or
[SDLNet_TCP_Accept](SDLNet_TCP_Accept.md).

This function sends `len` bytes, pointed to by `data` over the non-server
socket `sock`.

This function returns the actual amount of data sent. If the return value
is less than the amount of data sent, then either the remote connection was
closed, or an unknown socket error occurred.

This function may block!

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_TCP_Recv](SDLNet_TCP_Recv.md)

----
[CategoryAPI](CategoryAPI.md)
