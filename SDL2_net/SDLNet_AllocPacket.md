###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AllocPacket

Allocate a single UDP packet.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
UDPpacket * SDLNet_AllocPacket(int size);
```

## Function Parameters

|     |          |                                                                  |
| --- | -------- | ---------------------------------------------------------------- |
| int | **size** | the maximum number of bytes of payload this packet will contain. |

## Return Value

(UDPpacket *) Returns the new packet, or NULL if the function ran out of
memory.

## Remarks

This allocates a packet with `size` bytes of space for payload.

When done with this packet, you can free it with
[SDLNet_FreePacket](SDLNet_FreePacket). Packets can be reused multiple
times; you don't have to allocate a new one for each piece of data you
intend to send.

You can allocate multiple packets at once with
[SDLNet_AllocPacketV](SDLNet_AllocPacketV).

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_ResizePacket](SDLNet_ResizePacket)
- [SDLNet_FreePacket](SDLNet_FreePacket)
- [SDLNet_AllocPacketV](SDLNet_AllocPacketV)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

