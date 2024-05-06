###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_WaitUntilConnected

Block until a stream socket has connected to a server.

## Header File

Defined in SDL_net.h

## Syntax

```c
int SDLNet_WaitUntilConnected(SDLNet_StreamSocket *sock, Sint32 timeout);

```

## Function Parameters

|                 |                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| **sock**        | The [SDLNet_StreamSocket](SDLNet_StreamSocket) object to wait on.                                                    |
| **timeout**     | Number of milliseconds to wait for resolution to complete. -1 to wait indefinitely, 0 to check once without waiting. |

## Return Value

Returns 1 if successfully connected, -1 if connection failed, 0 if still
connecting (this function timed out without resolution); if -1, call
SDL_GetError() for details.

## Remarks

The [SDLNet_StreamSocket](SDLNet_StreamSocket) objects returned by
[SDLNet_CreateClient](SDLNet_CreateClient) take time to do their work, so
it is does so _asynchronously_ instead of making your program wait an
indefinite amount of time.

However, if you want your program to sleep until the connection is
complete, you can call this function.

This function takes a timeout value, represented in milliseconds, of how
long to wait for resolution to complete. Specifying a timeout of -1
instructs the library to wait indefinitely, and a timeout of 0 just checks
the current status and returns immediately (and is functionally equivalent
to calling [SDLNet_GetConnectionStatus](SDLNet_GetConnectionStatus)).

Connections can fail after some time (server took awhile to respond at all,
and then refused the connection outright), so be sure to check the result
of this function instead of assuming it worked!

Once a connection is successfully made, the socket may read data from, or
write data to, the connected server.

If you don't want your program to block, you can call
[SDLNet_GetConnectionStatus](SDLNet_GetConnectionStatus)() from time to
time until you get a non-zero result.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different socket at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_GetConnectionStatus](SDLNet_GetConnectionStatus)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

