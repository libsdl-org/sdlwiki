###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowDisplayIndex

Get the index of the display associated with a window.

## Syntax

```c
int SDL_GetWindowDisplayIndex(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the index of the display containing the center of the window on
success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetDisplayBounds](SDL_GetDisplayBounds.md)
* [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays.md)

----
[CategoryAPI](CategoryAPI.md)
