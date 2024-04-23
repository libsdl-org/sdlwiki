###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VERSIONNUM

This macro turns the version numbers into a numeric value:

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
#define SDL_VERSIONNUM(X, Y, Z)                     \
    ((X)*1000 + (Y)*100 + (Z))
```

## Remarks

```
(1,2,3) -> (1203)
```

This assumes that there will never be more than 100 patchlevels.

In versions higher than 2.9.0, the minor version overflows into the
thousands digit: for example, 2.23.0 is encoded as 4300, and 2.255.99 would
be encoded as 25799.

This macro will not be available in SDL 3.x.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)


