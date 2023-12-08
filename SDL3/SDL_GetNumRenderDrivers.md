###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_GetRenderDriver](SDL_GetRenderDriver.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
