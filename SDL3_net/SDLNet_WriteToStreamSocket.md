###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_WriteToStreamSocket

Send bytes over a stream socket to a remote system.

## Header File

Defined in SDL_net.h

## Syntax

```c
int SDLNet_WriteToStreamSocket(SDLNet_StreamSocket *sock, const void *buf, int buflen);

```

## Function Parameters

|                |                                         |
| -------------- | --------------------------------------- |
| **sock**       | the stream socket to send data through  |
| **buf**        | a pointer to the data to send.          |
| **buflen**     | the size of the data to send, in bytes. |

## Return Value

Returns 0 if data sent or queued for transmission, -1 on failure; call
SDL_GetError() for details.

## Remarks

Stream sockets are _reliable_, which means data sent over them will arrive
in the order it was transmitted, and the system will retransmit data as
necessary to ensure its delivery. Which is to say, short of catastrophic
failure, data will arrive, possibly with severe delays. Also, "catastrophic
failure" isn't an uncommon event.

(This is opposed to Datagram sockets, which send chunks of data that might
arrive in any order, or not arrive at all, but you never wait for missing
chunks to show up.)

Stream sockets are _bidirectional_; you can read and write from the same
stream, and the other end of the connection can, too.

This call never blocks; if it can't send the data immediately, the library
will queue it for later transmission. You can use
[SDLNet_GetStreamSocketPendingWrites](SDLNet_GetStreamSocketPendingWrites)()
to see how much is still queued for later transmission, or
[SDLNet_WaitUntilStreamSocketDrained](SDLNet_WaitUntilStreamSocketDrained)()
to block until all pending data has been sent.

If the connection has failed (remote side dropped us, or one of a million
other networking failures occurred), this function will report failure by
returning -1. Stream sockets only report failure for unrecoverable
conditions; once a stream socket fails, you should assume it is no longer
usable and should destroy it with SDL_DestroyStreamSocket().

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [SDLNet_GetStreamSocketPendingWrites](SDLNet_GetStreamSocketPendingWrites)
- [SDLNet_WaitUntilStreamSocketDrained](SDLNet_WaitUntilStreamSocketDrained)
- [SDLNet_ReadFromStreamSocket](SDLNet_ReadFromStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

