###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDesktopDisplayMode

Get information about the desktop's display mode.

## Syntax

```c
int SDL_GetDesktopDisplayMode(int displayIndex, SDL_DisplayMode * mode);

```

## Function Parameters

|                      |                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| **displayIndex**     | the index of the display to query                                                       |
| **mode**             | an [SDL_DisplayMode](SDL_DisplayMode) structure filled in with the current display mode |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

There's a difference between this function and
[SDL_GetCurrentDisplayMode](SDL_GetCurrentDisplayMode)() when SDL runs
fullscreen and has changed the resolution. In that case this function will
return the previous native display mode, and not the current display mode.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetCurrentDisplayMode](SDL_GetCurrentDisplayMode)
* [SDL_GetDisplayMode](SDL_GetDisplayMode)
* [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)


## Header

SDL_video.h

----
[CategoryAPI](CategoryAPI)

