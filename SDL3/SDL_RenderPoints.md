# SDL_RenderPoints

Draw multiple points on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderPoints(SDL_Renderer *renderer, const SDL_FPoint *points, int count);
```

## Function Parameters

|                                  |              |                                                 |
| -------------------------------- | ------------ | ----------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer** | the renderer which should draw multiple points. |
| const [SDL_FPoint](SDL_FPoint) * | **points**   | the points to draw.                             |
| int                              | **count**    | the number of points to draw.                   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderPoint](SDL_RenderPoint)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

