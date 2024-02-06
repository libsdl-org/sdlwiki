###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderColorScale

Set the color scale used for render operations.

## Syntax

```c
int SDL_SetRenderColorScale(SDL_Renderer *renderer, float scale);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |
| **scale**        | the color scale value |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The color scale is an additional scale multiplied into the pixel color
value while rendering. This can be used to adjust the brightness of colors
during HDR rendering, or changing HDR video brightness when playing on an
SDR display.

The color scale does not affect the alpha channel, only the color
brightness.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderColorScale](SDL_GetRenderColorScale)

----
[CategoryAPI](CategoryAPI)

