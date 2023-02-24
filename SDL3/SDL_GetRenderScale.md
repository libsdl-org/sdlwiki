###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderScale

Get the drawing scale for the current target.

## Syntax

```c
int SDL_GetRenderScale(SDL_Renderer *renderer, float *scaleX, float *scaleY);

```

## Function Parameters

|                  |                                                        |
| ---------------- | ------------------------------------------------------ |
| **renderer**     | the rendering context                                  |
| **scaleX**       | a pointer filled in with the horizontal scaling factor |
| **scaleY**       | a pointer filled in with the vertical scaling factor   |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderScale](SDL_SetRenderScale)

----
[CategoryAPI](CategoryAPI)

