###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_CreateClient

Begin connecting a socket as a client to a remote server.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
SDLNet_StreamSocket * SDLNet_CreateClient(SDLNet_Address *address, Uint16 port);
```

## Function Parameters

|                                    |             |                                                |
| ---------------------------------- | ----------- | ---------------------------------------------- |
| [SDLNet_Address](SDLNet_Address) * | **address** | the address of the remote server to connect to |
| Uint16                             | **port**    | the port on the remote server to connect to    |

## Return Value

([SDLNet_StreamSocket](SDLNet_StreamSocket) *) Returns a new
[SDLNet_StreamSocket](SDLNet_StreamSocket), pending connection, or NULL on
error; call SDL_GetError() for details.

## Remarks

Each [SDLNet_StreamSocket](SDLNet_StreamSocket) represents a single
connection between systems. Usually, a client app will have one connection
to a server app on a different computer, and the server app might have many
connections from different clients. Each of these connections communicate
over a separate stream socket.

Connecting is an asynchronous operation; this function does not block, and
will return before the connection is complete. One has to then use
[SDLNet_WaitUntilConnected](SDLNet_WaitUntilConnected)() or
[SDLNet_GetConnectionStatus](SDLNet_GetConnectionStatus)() to see when the
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
[SDLNet_DestroyStreamSocket](SDLNet_DestroyStreamSocket)().

Unlike BSD sockets or WinSock, you specify the port as a normal integer;
you do not have to byteswap it into "network order," as the library will
handle that for you.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_WaitUntilConnected](SDLNet_WaitUntilConnected)
- [SDLNet_GetConnectionStatus](SDLNet_GetConnectionStatus)
- [SDLNet_DestroyStreamSocket](SDLNet_DestroyStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

