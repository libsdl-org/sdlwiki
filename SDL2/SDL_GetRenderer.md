###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRenderer

Get the renderer associated with a window.

## Syntax

```c
SDL_Renderer * SDL_GetRenderer(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the rendering context on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI)

