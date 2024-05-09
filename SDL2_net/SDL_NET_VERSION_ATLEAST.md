###### (This function is part of SDL_net, a separate library from SDL.)
# SDL_NET_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_net at least X.Y.Z.

## Header File

Defined in SDL_net.h

## Syntax

```c
#define SDL_NET_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_NET_MAJOR_VERSION >= X) && \
     (SDL_NET_MAJOR_VERSION > X || SDL_NET_MINOR_VERSION >= Y) && \
     (SDL_NET_MAJOR_VERSION > X || SDL_NET_MINOR_VERSION > Y || SDL_NET_PATCHLEVEL >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

