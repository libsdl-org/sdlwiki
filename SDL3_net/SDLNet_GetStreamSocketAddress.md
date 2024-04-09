###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetStreamSocketAddress

Get the remote address of a stream socket.

## Header File

Defined in SDL_net.h

## Syntax

```c
SDLNet_Address * SDLNet_GetStreamSocketAddress(SDLNet_StreamSocket *sock);

```

## Function Parameters

|              |                            |
| ------------ | -------------------------- |
| **sock**     | the stream socket to query |

## Return Value

Returns the socket's remote address, or NULL on error; call SDL_GetError()
for details.

## Remarks

This reports the address of the remote side of a stream socket, which might
still be pending connnection.

This adds a reference to the address; the caller _must_ call
[SDLNet_UnrefAddress](SDLNet_UnrefAddress)() when done with it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

