###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_ResizePacket

Reallocate a UDP packet's payload space.

## Header File

Defined in [<SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/SDL2/include/SDL_net.h)

## Syntax

```c
int SDLNet_ResizePacket(UDPpacket *packet, int newsize);
```

## Function Parameters

|     |             |                                                                      |
| --- | ----------- | -------------------------------------------------------------------- |
| int | **newsize** | the new maximum number of bytes of payload this packet will contain. |

## Return Value

(int) Returns the new maximum payload size, which will be unchanged from
the previous if the system ran out of memory.

## Remarks

This takes an existing packet and makes sure it can contain at least
`newsize` bytes of space for payload.

When done with this packet, you can free it with
[SDLNet_FreePacket](SDLNet_FreePacket). Packets can be used multiple times;
you don't have to allocate a new one for each piece of data you intend to
send.

Please note that on memory allocation failure, this function will leave the
existing buffer alone, and _will return the original buffer size_. It will
not return an error value, it'll just leave the packet as it was!

**Warning**: Existing contents of the packet's data are lost when resizing,
whether you are growing or shrinking the payload space, since SDL_net does
not realloc the existing data.

## Version

This function is available since SDL_net 2.0.0.

## See Also

- [SDLNet_AllocPacket](SDLNet_AllocPacket)
- [SDLNet_FreePacket](SDLNet_FreePacket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

