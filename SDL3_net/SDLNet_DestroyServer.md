###### (This function is part of SDL_net, a separate library from SDL.)
# SDLNet_DestroyServer

Dispose of a previously-created server.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
void SDLNet_DestroyServer(SDLNet_Server *server);
```

## Function Parameters

|                                  |            |                   |
| -------------------------------- | ---------- | ----------------- |
| [SDLNet_Server](SDLNet_Server) * | **server** | server to destroy |

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

## See Also

- [SDLNet_CreateServer](SDLNet_CreateServer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

