###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_FreePacketV

Free a UDP packet vector (array of packets).

## Header File

Defined in SDL_net.h

## Syntax

```c
void SDLNet_FreePacketV(UDPpacket **packetV);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **packetV**     | the results of a call to [SDLNet_AllocPacketV](SDLNet_AllocPacketV)(). |

## Remarks

This frees the results of a previous call to
[SDLNet_AllocPacketV](SDLNet_AllocPacketV)(), freeing both the set of
packets and the array that holds them.

It is safe to free a NULL array through here; it's a harmless no-op.

You must not use this to free packets allocated through any function other
than [SDLNet_AllocPacketV](SDLNet_AllocPacketV)().

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_AllocPacketV](SDLNet_AllocPacketV)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

