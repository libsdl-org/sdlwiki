# SDL_RenderPoint

Draw a point on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderPoint(SDL_Renderer *renderer, float x, float y);
```

## Function Parameters

|                                |              |                                         |
| ------------------------------ | ------------ | --------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should draw a point. |
| float                          | **x**        | the x coordinate of the point.          |
| float                          | **y**        | the y coordinate of the point.          |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderPoints](SDL_RenderPoints)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

