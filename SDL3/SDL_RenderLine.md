###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RenderLine

Draw a line on the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderLine(SDL_Renderer *renderer, float x1, float y1, float x2, float y2);
```

## Function Parameters

|                                |              |                                        |
| ------------------------------ | ------------ | -------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer which should draw a line. |
| float                          | **x1**       | the x coordinate of the start point.   |
| float                          | **y1**       | the y coordinate of the start point.   |
| float                          | **x2**       | the x coordinate of the end point.     |
| float                          | **y2**       | the y coordinate of the end point.     |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

You may only call this function from the main thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderLines](SDL_RenderLines)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

