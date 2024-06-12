###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreePacket

Dispose of a UDP packet.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
void SDLNet_FreePacket(UDPpacket *packet);
```

## Function Parameters

|             |            |                     |
| ----------- | ---------- | ------------------- |
| UDPpacket * | **packet** | the packet to free. |

## Remarks

This frees both the packet's payload and the packet itself. Once this call
completes, the packet's pointer is invalid and should not be used anymore.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_AllocPacket](SDLNet_AllocPacket)
- [SDLNet_ResizePacket](SDLNet_ResizePacket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

