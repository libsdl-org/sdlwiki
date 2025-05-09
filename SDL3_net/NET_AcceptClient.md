###### (This function is part of SDL_net, a separate library from SDL.)
# NET_AcceptClient

Create a stream socket for the next pending client connection.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
bool NET_AcceptClient(NET_Server *server, NET_StreamSocket **client_stream);
```

## Function Parameters

|                                         |                   |                                                                                 |
| --------------------------------------- | ----------------- | ------------------------------------------------------------------------------- |
| [NET_Server](NET_Server) *              | **server**        | the server object to check for pending connections.                             |
| [NET_StreamSocket](NET_StreamSocket) ** | **client_stream** | Will be set to a new stream socket if a connection was pending, NULL otherwise. |

## Return Value

(bool) Returns true on success (even if no new connections were pending),
false on error; call SDL_GetError() for details.

## Remarks

When a client connects to a server, their connection will be pending until
the server _accepts_ the connection. Once accepted, the server will be
given a stream socket to communicate with the client, and they can send
data to, and receive data from, each other.

Unlike [NET_CreateClient](NET_CreateClient), stream sockets returned from
this function are already connected and do not have to wait for the
connection to complete, as server acceptance is the final step of
connecting.

This function does not block. If there are no new connections pending, this
function will return true (for success, but `*client_stream` will be set to
NULL. This is not an error and a common condition the app should expect. In
fact, this function should be called in a loop until this condition occurs,
so all pending connections are accepted in a single batch.

If you want the server to sleep until there's a new connection, you can use
[NET_WaitUntilInputAvailable](NET_WaitUntilInputAvailable)().

When done with the newly-accepted client, you can disconnect and dispose of
the stream socket by calling NET_DestroyStreamSocket().

## Thread Safety

You should not operate on the same server from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different servers at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [NET_WaitUntilInputAvailable](NET_WaitUntilInputAvailable)
- [NET_DestroyStreamSocket](NET_DestroyStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

