###### (This function is part of SDL_net, a separate library from SDL.)
# NET_WaitUntilStreamSocketDrained

Block until all of a stream socket's pending data is sent.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int NET_WaitUntilStreamSocketDrained(NET_StreamSocket *sock, Sint32 timeout);
```

## Function Parameters

|                                        |             |                                                                                                                    |
| -------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------ |
| [NET_StreamSocket](NET_StreamSocket) * | **sock**    | the stream socket to wait on.                                                                                      |
| Sint32                                 | **timeout** | Number of milliseconds to wait for draining to complete. -1 to wait indefinitely, 0 to check once without waiting. |

## Return Value

(int) Returns number of bytes still pending transmission, -1 on failure;
call SDL_GetError() for details.

## Remarks

If [NET_WriteToStreamSocket](NET_WriteToStreamSocket)() couldn't send all
its data immediately, it will queue it to be sent later. This function lets
the app sleep until all the data is transmitted.

This function takes a timeout value, represented in milliseconds, of how
long to wait for transmission to complete. Specifying a timeout of -1
instructs the library to wait indefinitely, and a timeout of 0 just checks
the current status and returns immediately (and is functionally equivalent
to calling
[NET_GetStreamSocketPendingWrites](NET_GetStreamSocketPendingWrites)).

If you don't want your program to block, you can call
[NET_GetStreamSocketPendingWrites](NET_GetStreamSocketPendingWrites) from
time to time until you get a result <= 0.

If the connection has failed (remote side dropped us, or one of a million
other networking failures occurred), this function will report failure by
returning -1. Stream sockets only report failure for unrecoverable
conditions; once a stream socket fails, you should assume it is no longer
usable and should destroy it with
[NET_DestroyStreamSocket](NET_DestroyStreamSocket)().

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## See Also

- [NET_WriteToStreamSocket](NET_WriteToStreamSocket)
- [NET_GetStreamSocketPendingWrites](NET_GetStreamSocketPendingWrites)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLNet](CategorySDLNet)

