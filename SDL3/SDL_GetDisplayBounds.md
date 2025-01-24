# SDL_GetDisplayBounds

Get the desktop area represented by a display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetDisplayBounds(SDL_DisplayID displayID, SDL_Rect *rect);
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

The primary display is often located at (0,0), but may be placed at a
different location depending on monitor layout.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetDisplayUsableBounds](SDL_GetDisplayUsableBounds)
- [SDL_GetDisplays](SDL_GetDisplays)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

