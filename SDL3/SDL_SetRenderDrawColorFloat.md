###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetRenderDrawColorFloat

Set the color used for drawing operations (Rect, Line and Clear).

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderDrawColorFloat(SDL_Renderer *renderer, float r, float g, float b, float a);
```

## Function Parameters

|                                |              |                                                                                                                                                              |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context.                                                                                                                                       |
| float                          | **r**        | the red value used to draw on the rendering target.                                                                                                          |
| float                          | **g**        | the green value used to draw on the rendering target.                                                                                                        |
| float                          | **b**        | the blue value used to draw on the rendering target.                                                                                                         |
| float                          | **a**        | the alpha value used to draw on the rendering target. Use [SDL_SetRenderDrawBlendMode](SDL_SetRenderDrawBlendMode) to specify how the alpha channel is used. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Set the color for drawing or filling rectangles, lines, and points, and for
[SDL_RenderClear](SDL_RenderClear)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetRenderDrawColorFloat](SDL_GetRenderDrawColorFloat)
- [SDL_SetRenderDrawColor](SDL_SetRenderDrawColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

