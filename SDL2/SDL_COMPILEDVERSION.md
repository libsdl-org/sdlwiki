###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_COMPILEDVERSION

This is the version number macro for the current SDL version.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
#define SDL_COMPILEDVERSION \
    SDL_VERSIONNUM(SDL_MAJOR_VERSION, SDL_MINOR_VERSION, SDL_PATCHLEVEL)
```

## Remarks

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300. This macro will
not be available in SDL 3.x.

Deprecated, use [SDL_VERSION_ATLEAST](SDL_VERSION_ATLEAST) or
[SDL_VERSION](SDL_VERSION) instead.

## Related Macros

:[[SDL_VERSIONNUM]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)


