###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetWindow

Get the window associated with a renderer.

## Syntax

```c
SDL_Window * SDL_RenderGetWindow(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the renderer to query |

## Return Value

Returns the window on success or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI.md)
