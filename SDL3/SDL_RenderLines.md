###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderLines

Draw a series of connected lines on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_RenderLines(SDL_Renderer *renderer, const SDL_FPoint *points, int count);
```

## Function Parameters

|                                  |              |                                                |
| -------------------------------- | ------------ | ---------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *   | **renderer** | the renderer which should draw multiple lines. |
| const [SDL_FPoint](SDL_FPoint) * | **points**   | the points along the lines.                    |
| int                              | **count**    | the number of points, drawing count-1 lines.   |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderLine](SDL_RenderLine)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

