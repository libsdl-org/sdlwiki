###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL at least X.Y.Z.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
#define SDL_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_MAJOR_VERSION >= X) && \
     (SDL_MAJOR_VERSION > X || SDL_MINOR_VERSION >= Y) && \
     (SDL_MAJOR_VERSION > X || SDL_MINOR_VERSION > Y || SDL_PATCHLEVEL >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)

