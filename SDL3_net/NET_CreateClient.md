###### (This function is part of SDL_net, a separate library from SDL.)
# NET_CreateClient

Begin connecting a socket as a client to a remote server.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
NET_StreamSocket * NET_CreateClient(NET_Address *address, Uint16 port);
```

## Function Parameters

|                              |             |                                                 |
| ---------------------------- | ----------- | ----------------------------------------------- |
| [NET_Address](NET_Address) * | **address** | the address of the remote server to connect to. |
| Uint16                       | **port**    | the port on the remote server to connect to.    |

## Return Value

([NET_StreamSocket](NET_StreamSocket) *) Returns a new
[NET_StreamSocket](NET_StreamSocket), pending connection, or NULL on error;
call SDL_GetError() for details.

## Remarks

Each [NET_StreamSocket](NET_StreamSocket) represents a single connection
between systems. Usually, a client app will have one connection to a server
app on a different computer, and the server app might have many connections
from different clients. Each of these connections communicate over a
separate stream socket.

Connecting is an asynchronous operation; this function does not block, and
will return before the connection is complete. One has to then use
[NET_WaitUntilConnected](NET_WaitUntilConnected)() or
[NET_GetConnectionStatus](NET_GetConnectionStatus)() to see when the
operation has completed, and if it was successful.

Once connected, you can read and write data to the returned socket. Stream
sockets are a mode of _reliable_ transmission, which means data will be
received as a stream of bytes in the order you sent it. If there are
problems in transmission, the system will deal with protocol negotiation
and retransmission as necessary, transparent to your app, but this means
until data is available in the order sent, the remote side will not get any
new data. This is the tradeoff vs datagram sockets, where data can arrive
in any order, or not arrive at all, without waiting, but the sender will
not know.

Stream sockets don't employ any protocol (above the TCP level), so they can
connect to servers that aren't using SDL_net, but if you want to speak any
protocol beyond an abritrary stream of bytes, such as HTTP, you'll have to
implement that yourself on top of the stream socket.

This function will fail if `address` is not finished resolving.

When you are done with this connection (whether it failed to connect or
not), you must dispose of it with
[NET_DestroyStreamSocket](NET_DestroyStreamSocket)().

Unlike BSD sockets or WinSock, you specify the port as a normal integer;
you do not have to byteswap it into "network order," as the library will
handle that for you.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_WaitUntilConnected](NET_WaitUntilConnected)
- [NET_GetConnectionStatus](NET_GetConnectionStatus)
- [NET_DestroyStreamSocket](NET_DestroyStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

