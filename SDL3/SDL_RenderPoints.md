###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderPoints

Draw multiple points on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderPoints(SDL_Renderer *renderer, const SDL_FPoint *points, int count);

```

## Function Parameters

|                  |                                                 |
| ---------------- | ----------------------------------------------- |
| **renderer**     | The renderer which should draw multiple points. |
| **points**       | The points to draw                              |
| **count**        | The number of points to draw                    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
