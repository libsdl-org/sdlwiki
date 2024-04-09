###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_DestroyDatagram

Dispose of a datagram packet previously received.

## Header File

Defined in SDL_net.h

## Syntax

```c
void SDLNet_DestroyDatagram(SDLNet_Datagram *dgram);

```

## Function Parameters

|               |                                 |
| ------------- | ------------------------------- |
| **dgram**     | the datagram packet to destroy. |

## Remarks

You must pass packets received through
[SDLNet_ReceiveDatagram](SDLNet_ReceiveDatagram) to this function when you
are done with them. This will free resources used by this packet and unref
its [SDLNet_Address](SDLNet_Address).

If you want to save the sender's address from the packet past this time, it
is safe to call [SDLNet_RefAddress](SDLNet_RefAddress)() on the address and
hold onto its pointer, so long as you call
[SDLNet_UnrefAddress](SDLNet_UnrefAddress)() on it when you are done with
it.

Once you call this function, the datagram pointer becomes invalid and
should not be used again by the app.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

