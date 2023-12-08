###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_DestroyServer

Dispose of a previously-created server.

## Syntax

```c
void SDLNet_DestroyServer(SDLNet_Server *server);

```

## Function Parameters

|                |                   |
| -------------- | ----------------- |
| **server**     | server to destroy |

## Remarks

This will immediately disconnect any pending client connections that had
not yet been accepted, but will not disconnect any existing accepted
connections (which can still be used and must be destroyed separately).
Further attempts to make new connections to this server will fail on the
client side.

## Thread Safety

You should not operate on the same server from multiple threads at the same
time without supplying a serialization mechanism. However, different
threads may access different servers at the same time without problems.

## Version

This function is available since SDL_Net 3.0.0.

## Related Functions

* [SDLNet_CreateServer](SDLNet_CreateServer.md)

----
[CategoryAPI](CategoryAPI.md)
