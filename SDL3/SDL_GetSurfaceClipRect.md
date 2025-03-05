# SDL_GetSurfaceClipRect

Get the clipping rectangle for a surface.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
bool SDL_GetSurfaceClipRect(SDL_Surface *surface, SDL_Rect *rect);
```

## Function Parameters

|                              |             |                                                                                          |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **surface** | the [SDL_Surface](SDL_Surface) structure representing the surface to be clipped.         |
| [SDL_Rect](SDL_Rect) *       | **rect**    | an [SDL_Rect](SDL_Rect) structure filled in with the clipping rectangle for the surface. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

When `surface` is the destination of a blit, only the area within the clip
rectangle is drawn into.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetSurfaceClipRect](SDL_SetSurfaceClipRect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

