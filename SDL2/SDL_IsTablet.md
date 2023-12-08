###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsTablet

Query if the current device is a tablet.

## Syntax

```c
SDL_bool SDL_IsTablet(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the device is a tablet,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

If SDL can't determine this, it will return [SDL_FALSE](SDL_FALSE.md).

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI.md)
