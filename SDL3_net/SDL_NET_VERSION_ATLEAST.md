###### (This function is part of SDL_net, a separate library from SDL.)
# SDL_NET_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_net at least X.Y.Z.

## Header File

Defined in [<SDL3_net/SDL_net.h>](https://github.com/libsdl-org/SDL_net/blob/main/include/SDL3_net/SDL_net.h)

## Syntax

```c
#define SDL_NET_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_NET_MAJOR_VERSION >= X) && \
     (SDL_NET_MAJOR_VERSION > X || SDL_NET_MINOR_VERSION >= Y) && \
     (SDL_NET_MAJOR_VERSION > X || SDL_NET_MINOR_VERSION > Y || SDL_NET_MICRO_VERSION >= Z))
```

## Version

This macro is available since SDL_net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySDLNet](CategorySDLNet)

