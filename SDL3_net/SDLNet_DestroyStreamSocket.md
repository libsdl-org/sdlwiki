###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_DestroyStreamSocket

Dispose of a previously-created stream socket.

## Syntax

```c
void SDLNet_DestroyStreamSocket(SDLNet_StreamSocket *sock);  /* Destroy your sockets when finished with them. Does not block, handles shutdown internally. */

```

## Function Parameters

|              |                          |
| ------------ | ------------------------ |
| **sock**     | stream socket to destroy |

## Remarks

This will immediately disconnect the other side of the connection, if
necessary. Further attempts to read or write the socket on the remote end
will fail.

This will _abandon_ any data queued for sending that hasn't made it to the
socket. If you need this data to arrive, you should wait for it to transmit
before destroying the socket with
[SDLNet_GetStreamSocketPendingWrites](SDLNet_GetStreamSocketPendingWrites)()
or
[SDLNet_WaitUntilStreamSocketDrained](SDLNet_WaitUntilStreamSocketDrained)().
Any data that has arrived from the remote end of the connection that hasn't
been read yet is lost.

## Thread Safety

You should not operate on the same socket from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different sockets at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_CreateClient](SDLNet_CreateClient)
* [SDLNet_AcceptClient](SDLNet_AcceptClient)
* [SDLNet_GetStreamSocketPendingWrites](SDLNet_GetStreamSocketPendingWrites)
* [SDLNet_WaitUntilStreamSocketDrained](SDLNet_WaitUntilStreamSocketDrained)

----
[CategoryAPI](CategoryAPI)

