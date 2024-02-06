###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderColorScale

Get the color scale used for render operations.

## Syntax

```c
int SDL_GetRenderColorScale(SDL_Renderer *renderer, float *scale);

```

## Function Parameters

|                  |                                                        |
| ---------------- | ------------------------------------------------------ |
| **renderer**     | the rendering context                                  |
| **scale**        | a pointer filled in with the current color scale value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderColorScale](SDL_SetRenderColorScale)

----
[CategoryAPI](CategoryAPI)

