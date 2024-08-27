###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ConvertEventToRenderCoordinates

Convert the coordinates in an event to render coordinates.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_bool SDL_ConvertEventToRenderCoordinates(SDL_Renderer *renderer, SDL_Event *event);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |
| [SDL_Event](SDL_Event) *       | **event**    | the event to modify.   |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Touch coordinates are converted from normalized coordinates in the window
to non-normalized rendering coordinates.

Once converted, the coordinates may be outside the rendering area.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RenderCoordinatesFromWindow](SDL_RenderCoordinatesFromWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

