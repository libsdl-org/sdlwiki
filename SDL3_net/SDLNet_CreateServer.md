###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_CreateServer

Create a server, which listens for connections to accept.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
SDLNet_Server * SDLNet_CreateServer(SDLNet_Address *addr, Uint16 port);
```

## Function Parameters

|                                    |          |                                                            |
| ---------------------------------- | -------- | ---------------------------------------------------------- |
| [SDLNet_Address](SDLNet_Address) * | **addr** | the _local_ address to listen for connections on, or NULL. |
| Uint16                             | **port** | the port on the local address to listen for connections on |

## Return Value

([SDLNet_Server](SDLNet_Server) *) Returns a new
[SDLNet_StreamSocket](SDLNet_StreamSocket), pending connection, or NULL on
error; call SDL_GetError() for details.

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
[SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses)(), but almost always
you just want to specify NULL here, to listen on any address available to
the app.

After creating a server, you get stream sockets to talk to incoming client
connections by calling [SDLNet_AcceptClient](SDLNet_AcceptClient)().

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

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses)
- [SDLNet_AcceptClient](SDLNet_AcceptClient)
- [SDLNet_DestroyServer](SDLNet_DestroyServer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

