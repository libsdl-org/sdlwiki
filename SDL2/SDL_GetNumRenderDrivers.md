###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumRenderDrivers

Get the number of 2D rendering drivers available for the current display.

## Syntax

```c
int SDL_GetNumRenderDrivers(void);

```

## Return Value

Returns a number >= 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

A render driver is a set of code that handles rendering and texture
management on a particular display. Normally there is only one, but some
drivers may have several available with different capabilities.

There may be none if SDL was compiled without render support.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_GetRenderDriverInfo](SDL_GetRenderDriverInfo.md)

----
[CategoryAPI](CategoryAPI.md)
