###### (This function is part of SDL_net, a separate library from SDL.)
# NET_StreamSocket

An object that represents a streaming connection to another system.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef struct NET_StreamSocket NET_StreamSocket;
```

## Remarks

This is meant to be a reliable, stream-oriented connection, such as TCP.

Each [NET_StreamSocket](NET_StreamSocket) represents a single connection
between systems. Usually, a client app will have one connection to a server
app on a different computer, and the server app might have many connections
from different clients. Each of these connections communicate over a
separate stream socket.

## Version

This datatype is available since SDL_net 3.0.0.

## See Also

- [NET_CreateClient](NET_CreateClient)
- [NET_WriteToStreamSocket](NET_WriteToStreamSocket)
- [NET_ReadFromStreamSocket](NET_ReadFromStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLNet](CategorySDLNet)

