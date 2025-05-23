# SDL_GetDisplayUsableBounds

Get the usable desktop area represented by a display, in screen coordinates.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetDisplayUsableBounds(SDL_DisplayID displayID, SDL_Rect *rect);
```

## Function Parameters

|                                |               |                                                                       |
| ------------------------------ | ------------- | --------------------------------------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query.                              |
| [SDL_Rect](SDL_Rect) *         | **rect**      | the [SDL_Rect](SDL_Rect) structure filled in with the display bounds. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is the same area as [SDL_GetDisplayBounds](SDL_GetDisplayBounds)()
reports, but with portions reserved by the system removed. For example, on
Apple's macOS, this subtracts the area occupied by the menu bar and dock.

Setting a window to be fullscreen generally bypasses these unusable areas,
so these are good guidelines for the maximum space available to a
non-fullscreen window.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

