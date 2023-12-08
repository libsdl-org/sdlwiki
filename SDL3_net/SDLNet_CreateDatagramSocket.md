###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_CreateDatagramSocket

Create and bind a new datagram socket.

## Syntax

```c
SDLNet_DatagramSocket * SDLNet_CreateDatagramSocket(SDLNet_Address *addr, Uint16 port);

```

## Function Parameters

|                 |                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------- |
| **address**     | the _local_ address to listen for connections on, or NULL.                                |
| **the**         | port on the local address to listen for connections on, or zero for the system to decide. |

## Return Value

Returns a new [SDLNet_DatagramSocket](SDLNet_DatagramSocket.md), or NULL on
error; call SDL_GetError() for details.

## Remarks

Datagram sockets follow different rules than stream sockets. They are not a
reliable stream of bytes but rather packets, they are not limited to
talking to a single other remote system, they do not maintain a single
"connection" that can be dropped, and they more nimble about network
failures at the expense of being more complex to use. What makes sense for
your app depends entirely on what your app is trying to accomplish.

Generally the idea of a datagram socket is that you send data one chunk
("packet") at a time to any address you want, and it arrives whenever it
gets there, even if later packets get there first, and maybe it doesn't get
there at all, and you don't know when anything of this happens by default.

This function creates a new datagram socket.

This function does not block, and is not asynchronous, as the system can
decide immediately if it can create a socket or not. If this returns
success, you can immediately start talking to the network.

You can specify an address to listen for connections on; this address must
be local to the system, and probably one returned by
[SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses.md)(), but almost always
you just want to specify NULL here, to listen on any address available to
the app.

If you need to bind to a specific port (like a server), you should specify
it in the `port` argument; datagram servers should do this, so they can be
reached at a well-known port. If you only plan to initiate communications
(like a client), you should specify 0 and let the system pick an unused
port. Only one process can bind to a specific port at a time, so if you
aren't acting as a server, you should choose 0. Datagram sockets can send
individual packets to any port, so this just declares where data will
arrive for your socket.

Datagram sockets don't employ any protocol (above the UDP level), so they
can talk to apps that aren't using SDL_net, but if you want to speak any
protocol beyond arbitrary packets of bytes, such as WebRTC, you'll have to
implement that yourself on top of the stream socket.

Unlike BSD sockets or WinSock, you specify the port as a normal integer;
you do not have to byteswap it into "network order," as the library will
handle that for you.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_GetLocalAddresses](SDLNet_GetLocalAddresses.md)
* [SDLNet_DestroyDatagramSocket](SDLNet_DestroyDatagramSocket.md)

----
[CategoryAPI](CategoryAPI.md)
