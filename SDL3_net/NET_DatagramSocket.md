###### (This function is part of SDL_net, a separate library from SDL.)
# NET_DatagramSocket

An object that represents a datagram connection to another system.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef struct NET_DatagramSocket NET_DatagramSocket;
```

## Remarks

This is meant to be an unreliable, packet-oriented connection, such as UDP.

Datagram sockets follow different rules than stream sockets. They are not a
reliable stream of bytes but rather packets, they are not limited to
talking to a single other remote system, they do not maintain a single
"connection" that can be dropped, and they are more nimble about network
failures at the expense of being more complex to use. What makes sense for
your app depends entirely on what your app is trying to accomplish.

Generally the idea of a datagram socket is that you send data one chunk
("packet") at a time to any address you want, and it arrives whenever it
gets there, even if later packets get there first, and maybe it doesn't get
there at all, and you don't know when anything of this happens by default.

## Version

This datatype is available since SDL_Net 3.0.0.

## See Also

- [NET_CreateDatagramSocket](NET_CreateDatagramSocket)
- [NET_SendDatagram](NET_SendDatagram)
- [NET_ReceiveDatagram](NET_ReceiveDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLNet](CategorySDLNet)

