###### (This function is part of SDL_net, a separate library from SDL.)
# NET_GetStreamSocketAddress

Get the remote address of a stream socket.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
NET_Address * NET_GetStreamSocketAddress(NET_StreamSocket *sock);
```

## Function Parameters

|                                        |          |                             |
| -------------------------------------- | -------- | --------------------------- |
| [NET_StreamSocket](NET_StreamSocket) * | **sock** | the stream socket to query. |

## Return Value

([NET_Address](NET_Address) *) Returns the socket's remote address, or NULL
on error; call SDL_GetError() for details.

## Remarks

This reports the address of the remote side of a stream socket, which might
still be pending connnection.

This adds a reference to the address; the caller _must_ call
[NET_UnrefAddress](NET_UnrefAddress)() when done with it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

