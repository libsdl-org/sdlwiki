###### (This function is part of SDL_net, a separate library from SDL.)
# NET_CreateServer

Create a server, which listens for connections to accept.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
NET_Server * NET_CreateServer(NET_Address *addr, Uint16 port);
```

## Function Parameters

|                              |          |                                                             |
| ---------------------------- | -------- | ----------------------------------------------------------- |
| [NET_Address](NET_Address) * | **addr** | the _local_ address to listen for connections on, or NULL.  |
| Uint16                       | **port** | the port on the local address to listen for connections on. |

## Return Value

([NET_Server](NET_Server) *) Returns a new [NET_Server](NET_Server), or
NULL on error; call SDL_GetError() for details.

## Remarks

An app that initiates connection to a remote computer is called a "client,"
and the thing the client connects to is called a "server."

Servers listen for and accept connections from clients, which spawns a new
stream socket on the server's end, which it can then send/receive data on.

Use this function to create a server that will accept connections from
other systems.

This function does not block, and is not asynchronous, as the system can
decide immediately if it can create a server or not. If this returns
success, you can immediately start accepting connections.

You can specify an address to listen for connections on; this address must
be local to the system, and probably one returned by
[NET_GetLocalAddresses](NET_GetLocalAddresses)(), but almost always you
just want to specify NULL here, to listen on any address available to the
app.

After creating a server, you get stream sockets to talk to incoming client
connections by calling [NET_AcceptClient](NET_AcceptClient)().

Stream sockets don't employ any protocol (above the TCP level), so they can
accept connections from clients that aren't using SDL_net, but if you want
to speak any protocol beyond an abritrary stream of bytes, such as HTTP,
you'll have to implement that yourself on top of the stream socket.

Unlike BSD sockets or WinSock, you specify the port as a normal integer;
you do not have to byteswap it into "network order," as the library will
handle that for you.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_net 3.0.0.

## See Also

- [NET_GetLocalAddresses](NET_GetLocalAddresses)
- [NET_AcceptClient](NET_AcceptClient)
- [NET_DestroyServer](NET_DestroyServer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

