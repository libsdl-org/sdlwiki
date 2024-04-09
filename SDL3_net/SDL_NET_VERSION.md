###### (This function is part of SDL_net, a separate library from SDL.)
# SDL_NET_VERSION

Query the verion of the SDL_net library in use at compile time.

## Header File

Defined in SDL_net.h

## Syntax

```c
#define SDL_NET_VERSION(X)                          \
{                                                   \
    (X)->major = SDL_NET_MAJOR_VERSION;             \
    (X)->minor = SDL_NET_MINOR_VERSION;             \
    (X)->patch = SDL_NET_PATCHLEVEL;                \
}
```

## Remarks

This macro copies the version listen in the SDL_net headers into a struct
of the app's choosing.

## Thread Safety

It is safe to use this macro from any thread.

## Version

This macro is available since SDL_Net 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

