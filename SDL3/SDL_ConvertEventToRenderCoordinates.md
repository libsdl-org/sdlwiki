###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertEventToRenderCoordinates

Convert the coordinates in an event to render coordinates.

## Syntax

```c
int SDL_ConvertEventToRenderCoordinates(SDL_Renderer *renderer, SDL_Event *event);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |
| **event**        | the event to modify   |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Touch coordinates are converted from normalized coordinates in the window
to non-normalized rendering coordinates.

Once converted, the coordinates may be outside the rendering area.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderCoordinatesFromWindowCoordinates](SDL_GetRenderCoordinatesFromWindowCoordinates)

----
[CategoryAPI](CategoryAPI)

