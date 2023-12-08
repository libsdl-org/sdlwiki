###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreePacket

Dispose of a UDP packet.

## Syntax

```c
void SDLNet_FreePacket(UDPpacket *packet);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **packet**     | the packet to free. |

## Remarks

This frees both the packet's payload and the packet itself. Once this call
completes, the packet's pointer is invalid and should not be used anymore.

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_AllocPacket](SDLNet_AllocPacket.md)
* [SDLNet_ResizePacket](SDLNet_ResizePacket.md)

----
[CategoryAPI](CategoryAPI.md)
