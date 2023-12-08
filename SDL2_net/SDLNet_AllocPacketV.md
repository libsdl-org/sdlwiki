###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_AllocPacketV

Allocate a UDP packet vector (array of packets).

## Syntax

```c
UDPpacket ** SDLNet_AllocPacketV(int howmany, int size);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **howmany**     | the number of packets to allocate.                       |
| **size**        | the maximum bytes of payload each packet should contain. |

## Return Value

Returns a pointer to the first packet in the array, or NULL if the function
ran out of memory.

## Remarks

This allocates `howmany` packets at once, each `size` bytes long.

You must free the results of this function with
[SDLNet_FreePacketV](SDLNet_FreePacketV.md), and must not free individual
packets from this function with [SDLNet_FreePacket](SDLNet_FreePacket.md).

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_FreePacketV](SDLNet_FreePacketV.md)

----
[CategoryAPI](CategoryAPI.md)
