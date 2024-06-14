###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_GetStreamSocketPendingWrites

Query bytes still pending transmission on a stream socket.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
int SDLNet_GetStreamSocketPendingWrites(SDLNet_StreamSocket *sock);
```

## Function Parameters

|                                              |          |                             |
| -------------------------------------------- | -------- | --------------------------- |
| [SDLNet_StreamSocket](SDLNet_StreamSocket) * | **sock** | the stream socket to query. |

## Return Value

(int) Returns number of bytes still pending transmission, -1 on failure;
call SDL_GetError() for details.

## Remarks

If [SDLNet_WriteToStreamSocket](SDLNet_WriteToStreamSocket)() couldn't send
all its data immediately, it will queue it to be sent later. This function
lets the app see how much of that queue is still pending to be sent.

The library will try to send more queued data before reporting what's left,
but it will not block to do so.

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
- [SDLNet_WaitUntilStreamSocketDrained](SDLNet_WaitUntilStreamSocketDrained)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

