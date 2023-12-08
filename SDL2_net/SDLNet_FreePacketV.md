###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreePacketV

Free a UDP packet vector (array of packets).

## Syntax

```c
void SDLNet_FreePacketV(UDPpacket **packetV);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **packetV**     | the results of a call to [SDLNet_AllocPacketV](SDLNet_AllocPacketV.md)(). |

## Remarks

This frees the results of a previous call to
[SDLNet_AllocPacketV](SDLNet_AllocPacketV.md)(), freeing both the set of
packets and the array that holds them.

It is safe to free a NULL array through here; it's a harmless no-op.

You must not use this to free packets allocated through any function other
than [SDLNet_AllocPacketV](SDLNet_AllocPacketV.md)().

## Version

This function is available since SDL_net 2.0.0.

## Related Functions

* [SDLNet_AllocPacketV](SDLNet_AllocPacketV.md)

----
[CategoryAPI](CategoryAPI.md)
