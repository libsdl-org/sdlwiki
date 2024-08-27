###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderRects

Draw some number of rectangles on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_RenderRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count);
```

## Function Parameters

|                                |              |                                                     |
| ------------------------------ | ------------ | --------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should draw multiple rectangles. |
| const [SDL_FRect](SDL_FRect) * | **rects**    | a pointer to an array of destination rectangles.    |
| int                            | **count**    | the number of rectangles.                           |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderRect](SDL_RenderRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

