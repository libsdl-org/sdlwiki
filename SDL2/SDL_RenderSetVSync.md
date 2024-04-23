###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderSetVSync

Toggle VSync of the given renderer.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderSetVSync(SDL_Renderer* renderer, int vsync);

```

## Function Parameters

|                  |                                                    |
| ---------------- | -------------------------------------------------- |
| **renderer**     | The renderer to toggle                             |
| **vsync**        | 1 for on, 0 for off. All other values are reserved |

## Return Value

Returns a 0 int on success, or non-zero on failure

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

