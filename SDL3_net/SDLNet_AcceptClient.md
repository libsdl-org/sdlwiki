###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AcceptClient

Create a stream socket for the next pending client connection.

## Header File

Defined in SDL_net.h

## Syntax

```c
int SDLNet_AcceptClient(SDLNet_Server *server, SDLNet_StreamSocket **client_stream);

```

## Function Parameters

|                       |                                                                                 |
| --------------------- | ------------------------------------------------------------------------------- |
| **server**            | the server object to check for pending connections                              |
| **client_stream**     | Will be set to a new stream socket if a connection was pending, NULL otherwise. |

## Return Value

Returns 0 on success (even if no new connections were pending), -1 on
error; call SDL_GetError() for details.

## Remarks

When a client connects to a server, their connection will be pending until
the server _accepts_ the connection. Once accepted, the server will be
given a stream socket to communicate with the client, and they can send
data to, and receive data from, each other.

Unlike [SDLNet_CreateClient](SDLNet_CreateClient), stream sockets returned
from this function are already connected and do not have to wait for the
connection to complete, as server acceptance is the final step of
connecting.

This function does not block. If there are no new connections pending, this
function will return 0 (for success, but `*client_stream` will be set to
NULL. This is not an error and a common condition the app should expect. In
fact, this function should be called in a loop until this condition occurs,
so all pending connections are accepted in a single batch.

If you want the server to sleep until there's a new connection, you can use
[SDLNet_WaitUntilInputAvailable](SDLNet_WaitUntilInputAvailable)().

When done with the newly-accepted client, you can disconnect and dispose of
the stream socket by calling SDL_DestroyStreamSocket().

## Thread Safety

You should not operate on the same server from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different servers at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_WaitUntilInputAvailable](SDLNet_WaitUntilInputAvailable)
- [SDLNet_DestroyStreamSocket](SDLNet_DestroyStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

