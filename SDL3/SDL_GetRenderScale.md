###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderScale

Get the drawing scale for the current target.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_GetRenderScale(SDL_Renderer *renderer, float *scaleX, float *scaleY);
```

## Function Parameters

|                                |              |                                                         |
| ------------------------------ | ------------ | ------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                  |
| float *                        | **scaleX**   | a pointer filled in with the horizontal scaling factor. |
| float *                        | **scaleY**   | a pointer filled in with the vertical scaling factor.   |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetRenderScale](SDL_SetRenderScale)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

