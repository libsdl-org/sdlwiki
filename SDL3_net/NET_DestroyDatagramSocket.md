###### (This function is part of SDL_net, a separate library from SDL.)
# NET_DestroyDatagramSocket

Dispose of a previously-created datagram socket.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void NET_DestroyDatagramSocket(NET_DatagramSocket *sock);
```

## Function Parameters

|                                            |          |                             |
| ------------------------------------------ | -------- | --------------------------- |
| [NET_DatagramSocket](NET_DatagramSocket) * | **sock** | datagram socket to destroy. |

## Remarks

This will _abandon_ any data queued for sending that hasn't made it to the
socket. If you need this data to arrive, you should wait for confirmation
from the remote computer in some form that you devise yourself. Queued data
is not guaranteed to arrive even if the library made efforts to transmit it
here.

Any data that has arrived from the remote end of the connection that hasn't
been read yet is lost.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [NET_CreateDatagramSocket](NET_CreateDatagramSocket)
- [NET_SendDatagram](NET_SendDatagram)
- [NET_ReceiveDatagram](NET_ReceiveDatagram)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

