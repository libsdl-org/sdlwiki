# SDL_ConvertEventToRenderCoordinates

Convert the coordinates in an event to render coordinates.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_ConvertEventToRenderCoordinates(SDL_Renderer *renderer, SDL_Event *event);
```

## Function Parameters

|                                |              |                        |
| ------------------------------ | ------------ | ---------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the rendering context. |
| [SDL_Event](SDL_Event) *       | **event**    | the event to modify.   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This takes into account several states:

- The window dimensions.
- The logical presentation settings
  ([SDL_SetRenderLogicalPresentation](SDL_SetRenderLogicalPresentation))
- The scale ([SDL_SetRenderScale](SDL_SetRenderScale))
- The viewport ([SDL_SetRenderViewport](SDL_SetRenderViewport))

Various event types are converted with this function: mouse, touch, pen,
etc.

Touch coordinates are converted from normalized coordinates in the window
to non-normalized rendering coordinates.

Relative mouse coordinates (xrel and yrel event fields) are _also_
converted. Applications that do not want these fields converted should use
[SDL_RenderCoordinatesFromWindow](SDL_RenderCoordinatesFromWindow)() on the
specific event fields instead of converting the entire event structure.

Once converted, coordinates may be outside the rendering area.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_RenderCoordinatesFromWindow](SDL_RenderCoordinatesFromWindow)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

