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

## Code Examples

```c++
if (! SDL_VERSION_ATLEAST(2,0,0)) {
    SDL_Log("SDL_VERSION %i is less than 2.0.0", SDL_MAJOR_VERSION);
    return 1;
}
```

## Related Macros

[SDL_COMPILEDVERSION](SDL_COMPILEDVERSION)
[SDL_VERSIONNUM](SDL_VERSIONNUM)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)


