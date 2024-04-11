###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderGetLogicalSize

Get device independent resolution for rendering.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_RenderGetLogicalSize(SDL_Renderer * renderer, int *w, int *h);

```

## Function Parameters

|                  |                                     |
| ---------------- | ----------------------------------- |
| **renderer**     | a rendering context                 |
| **w**            | an int to be filled with the width  |
| **h**            | an int to be filled with the height |

## Remarks

When using the main rendering target (eg no target texture is set): this
may return 0 for `w` and `h` if the [SDL_Renderer](SDL_Renderer) has never
had its logical size set by
[SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize)(). Otherwise it
returns the logical width and height.

When using a target texture: Never return 0 for `w` and `h` at first. Then
it returns the logical width and height that are set.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

