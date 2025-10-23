# SDL_SetSurfaceClipRect

Set the clipping rectangle for a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_SetSurfaceClipRect(SDL_Surface *surface, const SDL_Rect *rect);
```

## Function Parameters

|                              |             |                                                                                                      |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure to be clipped.                                              |
| const [SDL_Rect](SDL_Rect) * | **rect**    | the [SDL_Rect](SDL_Rect) structure representing the clipping rectangle, or NULL to disable clipping. |

## Return Value

(bool) Returns true if the rectangle intersects the surface, otherwise
false and blits will be completely clipped.

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

Note that blits are automatically clipped to the edges of the source and
destination surfaces.

## Thread Safety

This function can be called on different threads with different surfaces.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetSurfaceClipRect](SDL_GetSurfaceClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

