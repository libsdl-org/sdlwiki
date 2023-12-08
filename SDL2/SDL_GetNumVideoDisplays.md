###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumVideoDisplays

Get the number of available video displays.

## Syntax

```c
int SDL_GetNumVideoDisplays(void);

```

## Return Value

Returns a number >= 1 or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetDisplayBounds](SDL_GetDisplayBounds.md)

----
[CategoryAPI](CategoryAPI.md)
