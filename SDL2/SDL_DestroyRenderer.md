###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyRenderer

Destroy the rendering context for a window and free associated textures.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

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
[SDL_GetError](SDL_GetError)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateRenderer](SDL_CreateRenderer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

