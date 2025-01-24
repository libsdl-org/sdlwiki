# SDL_GetCurrentDisplayMode

Get information about the current display mode.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_DisplayMode * SDL_GetCurrentDisplayMode(SDL_DisplayID displayID);
```

## Function Parameters

|                                |               |                                          |
| ------------------------------ | ------------- | ---------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query. |

## Return Value

(const [SDL_DisplayMode](SDL_DisplayMode) *) Returns a pointer to the
desktop display mode or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

There's a difference between this function and
[SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)() when SDL runs
fullscreen and has changed the resolution. In that case this function will
return the current display mode, and not the previous native display mode.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode)
- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

