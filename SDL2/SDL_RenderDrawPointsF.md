###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_RenderDrawPointsF

Draw multiple points on the current rendering target at subpixel precision.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderDrawPointsF(SDL_Renderer * renderer,
                          const SDL_FPoint * points,
                          int count);
```

## Function Parameters

|                                  |              |                                                 |
| -------------------------------- | ------------ | ----------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer** | The renderer which should draw multiple points. |
| const [SDL_FPoint](SDL_FPoint) * | **points**   | The points to draw.                             |
| int                              | **count**    | The number of points to draw.                   |

## Return Value

(int) Return 0 on success, or -1 on error.

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

