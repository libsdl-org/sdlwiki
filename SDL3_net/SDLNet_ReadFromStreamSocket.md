###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_ReadFromStreamSocket

Receive bytes that a remote system sent to a stream socket.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_ReadFromStreamSocket(SDLNet_StreamSocket *sock, void *buf, int buflen);
```

## Function Parameters

|                                              |            |                                                                                                                     |
| -------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| [SDLNet_StreamSocket](SDLNet_StreamSocket) * | **sock**   | the stream socket to receive data from.                                                                             |
| void *                                       | **buf**    | a pointer to a buffer where received data will be collected.                                                        |
| int                                          | **buflen** | the size of the buffer pointed to by `buf`, in bytes. This is the maximum that will be read from the stream socket. |

## Return Value

(int) Returns number of bytes read from the stream socket (which can be
less than `buflen` or zero if none available), -1 on failure; call
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

This function returns data that has arrived for the stream socket that
hasn't been read yet. Data is provided in the order it was sent on the
remote side. This function may return less data than requested, depending
on what is available at the time, and also the app isn't required to read
all available data at once.

This call never blocks; if no new data isn't available at the time of the
call, it returns 0 immediately. The caller can try again later.

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

- [SDLNet_WriteToStreamSocket](SDLNet_WriteToStreamSocket)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

