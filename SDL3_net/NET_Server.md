###### (This function is part of SDL_net, a separate library from SDL.)
# NET_Server

The receiving end of a stream connection.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef struct NET_Server NET_Server;
```

## Remarks

This is an opaque datatype, to be treated by the app as a handle.

Internally, this is what BSD sockets refers to as a "listen socket".
Clients attempt to connect to a server, and if the server accepts the
connection, will provide the app with a stream socket to send and receive
data over that connection.

## Version

This datatype is available since SDL_net 3.0.0.

## See Also

- [NET_CreateServer](NET_CreateServer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLNet](CategorySDLNet)

