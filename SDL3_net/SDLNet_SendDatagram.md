###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_SendDatagram

Send a new packet over a datagram socket to a remote system.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_SendDatagram(SDLNet_DatagramSocket *sock, SDLNet_Address *address, Uint16 port, const void *buf, int buflen);
```

## Function Parameters

|                                                  |             |                                                      |
| ------------------------------------------------ | ----------- | ---------------------------------------------------- |
| [SDLNet_DatagramSocket](SDLNet_DatagramSocket) * | **sock**    | the datagram socket to send data through             |
| [SDLNet_Address](SDLNet_Address) *               | **address** | the [SDLNet_Address](SDLNet_Address) object address. |
| Uint16                                           | **port**    | the address port.                                    |
| const void *                                     | **buf**     | a pointer to the data to send as a single packet.    |
| int                                              | **buflen**  | the size of the data to send, in bytes.              |

## Return Value

(int) Returns 0 if data sent or queued for transmission, -1 on failure;
call SDL_GetError() for details.

## Remarks

Datagram sockets send packets of data. They either arrive as complete
packets or they don't arrive at all, as opposed to stream sockets, where
individual bytes might trickle in as they attempt to reliably deliver a
stream of data.

Datagram packets might arrive in a different order than you sent them, or
they may just be lost while travelling across the network. You have to plan
for this.

You can send to any address and port on the network, but there has to be a
datagram socket waiting for the data on the other side for the packet not
to be lost.

General wisdom is that you shouldn't send a packet larger than 1500 bytes
over the Internet, as bad routers might fragment or lose larger ones, but
this limit is not hardcoded into SDL_net and in good conditions you might
be able to send significantly more.

This call never blocks; if it can't send the data immediately, the library
will queue it for later transmission. There is no query to see what is
still queued, as datagram transmission is unreliable, so you should never
assume anything about queued data.

If there's a fatal error, this function will return -1. Datagram sockets
generally won't report failures, because there is no state like a
"connection" to fail at this level, but may report failure for
unrecoverable system-level conditions; once a datagram socket fails, you
should assume it is no longer usable and should destroy it with
SDL_DestroyDatagramSocket().

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_ReceiveDatagram](SDLNet_ReceiveDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

