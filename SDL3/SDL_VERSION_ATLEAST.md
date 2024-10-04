###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL at least X.Y.Z.

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
#define SDL_VERSION_ATLEAST(X, Y, Z) \
    (SDL_VERSION >= SDL_VERSIONNUM(X, Y, Z))
```

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)

