###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyRenderer

Destroy the rendering context for a window and free associated textures.

## Syntax

```c
void SDL_DestroyRenderer(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Remarks

If `renderer` is NULL, this function will return immediately after setting
the SDL error message to "Invalid renderer". See
[SDL_GetError](SDL_GetError.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)

----
[CategoryAPI](CategoryAPI.md)
