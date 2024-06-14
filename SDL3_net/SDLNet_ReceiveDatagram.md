###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_ReceiveDatagram

Receive a new packet that a remote system sent to a datagram socket.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_ReceiveDatagram(SDLNet_DatagramSocket *sock, SDLNet_Datagram **dgram);
```

## Function Parameters

|                                                  |           |                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- |
| [SDLNet_DatagramSocket](SDLNet_DatagramSocket) * | **sock**  | the datagram socket to send data through. |
| [SDLNet_Datagram](SDLNet_Datagram) **            | **dgram** | a pointer to the datagram packet pointer. |

## Return Value

(int) Returns 0 if data sent or queued for transmission, -1 on failure;
call SDL_GetError() for details.

## Remarks

Datagram sockets send packets of data. They either arrive as complete
packets or they don't arrive at all, so you'll never receive half a packet.

This call never blocks; if no new data isn't available at the time of the
call, it returns 0 immediately. The caller can try again later.

On a successful call to this function, it returns zero, even if no new
packets are available, so you should check for a successful return and a
non-NULL value in `*dgram` to decide if a new packet is available.

You must pass received packets to
[SDLNet_DestroyDatagram](SDLNet_DestroyDatagram) when you are done with
them. If you want to save the sender's address past this time, it is safe
to call [SDLNet_RefAddress](SDLNet_RefAddress)() on the address and hold
onto the pointer, so long as you call
[SDLNet_UnrefAddress](SDLNet_UnrefAddress)() on it when you are done with
it.

Since datagrams can arrive from any address or port on the network without
prior warning, this information is available in the
[SDLNet_Datagram](SDLNet_Datagram) object that is provided by this
function, and this is the only way to know who to reply to. Even if you
aren't acting as a "server," packets can still arrive at your socket if
someone sends one.

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

- [SDLNet_SendDatagram](SDLNet_SendDatagram)
- [SDLNet_DestroyDatagram](SDLNet_DestroyDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

