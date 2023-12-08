###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderClear

Clear the current rendering target with the drawing color.

## Syntax

```c
int SDL_RenderClear(SDL_Renderer * renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function clears the entire rendering target, ignoring the viewport and
the clip rectangle.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor.md)

----
[CategoryAPI](CategoryAPI.md)
