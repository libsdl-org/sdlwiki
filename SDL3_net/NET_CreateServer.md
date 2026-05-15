###### (This function is part of SDL_net, a separate library from SDL.)
# NET_CreateServer

Create a server, which listens for connections to accept.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
NET_Server * NET_CreateServer(NET_Address *addr, Uint16 port, SDL_PropertiesID props);


#define NET_PROP_SERVER_REUSEADDR_BOOLEAN     "NET.server.reuseaddr"
```

## Function Parameters

|                              |           |                                                             |
| ---------------------------- | --------- | ----------------------------------------------------------- |
| [NET_Address](NET_Address) * | **addr**  | the _local_ address to listen for connections on, or NULL.  |
| Uint16                       | **port**  | the port on the local address to listen for connections on. |
| SDL_PropertiesID             | **props** | properties of the new server. Specify zero for defaults.    |

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

The caller may supply properties to customize behavior. This is optional,
and a value of zero for `props` will request defaults for all properties.

These are the supported properties:

- [`NET_PROP_SERVER_REUSEADDR_BOOLEAN`](NET_PROP_SERVER_REUSEADDR_BOOLEAN):
  true if the server should be created even if a previous server has
  recently used this address. For various reasons, networks prefer that
  there be some delay between apps reusing the same address, but this can
  be problematic when iterating quickly, for software development purposes
  or just restarting a crashed service. This property defaults to true
  (although it should be noted that, at the operating system level, this
  defaults to false!). If this property is false and the OS feels that not
  enough time has elapsed, server creation will fail and this function will
  report an error.

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

