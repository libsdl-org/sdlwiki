###### (This function is part of SDL_net, a separate library from SDL.)
# NET_Datagram

The data provided for new incoming packets from [NET_ReceiveDatagram](NET_ReceiveDatagram)().

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
typedef struct NET_Datagram
{
    NET_Address *addr;  /**< this is unref'd by NET_DestroyDatagram. You only need to ref it if you want to keep it. */
    Uint16 port;  /**< these do not have to come from the same port the receiver is bound to. These are in host byte order, don't byteswap them! */
    Uint8 *buf;  /**< the payload of this datagram. */
    int buflen;  /**< the number of bytes available at `buf`. */
} NET_Datagram;
```

## Version

This datatype is available since SDL_net 3.0.0.

## See Also

- [NET_ReceiveDatagram](NET_ReceiveDatagram)
- [NET_DestroyDatagram](NET_DestroyDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLNet](CategorySDLNet)

