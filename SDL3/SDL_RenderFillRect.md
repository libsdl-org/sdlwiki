###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderFillRect

Fill a rectangle on the current rendering target with the drawing color at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_RenderFillRect(SDL_Renderer *renderer, const SDL_FRect *rect);
```

## Function Parameters

|                                |              |                                                                                  |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should fill a rectangle.                                      |
| const [SDL_FRect](SDL_FRect) * | **rect**     | a pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderFillRects](SDL_RenderFillRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

