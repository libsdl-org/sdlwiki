###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRendererOutputSize

Get the output size in pixels of a rendering context.

## Syntax

```c
int SDL_GetRendererOutputSize(SDL_Renderer * renderer,
                              int *w, int *h);

```

## Function Parameters

|                  |                               |
| ---------------- | ----------------------------- |
| **renderer**     | the rendering context         |
| **w**            | an int filled with the width  |
| **h**            | an int filled with the height |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Due to high-dpi displays, you might end up with a rendering context that
has more pixels than the window that contains it, so use this instead of
[SDL_GetWindowSize](SDL_GetWindowSize.md)() to decide how much drawing area
you have.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRenderer](SDL_GetRenderer.md)

----
[CategoryAPI](CategoryAPI.md)
