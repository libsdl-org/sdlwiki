###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetCurrentDisplayMode

Get information about the current display mode.

## Syntax

```c
int SDL_GetCurrentDisplayMode(int displayIndex, SDL_DisplayMode * mode);

```

## Function Parameters

|                      |                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| **displayIndex**     | the index of the display to query                                                       |
| **mode**             | an [SDL_DisplayMode](SDL_DisplayMode.md) structure filled in with the current display mode |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

There's a difference between this function and
[SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode.md)() when SDL runs
fullscreen and has changed the resolution. In that case this function will
return the current display mode, and not the previous native display mode.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetDesktopDisplayMode](SDL_GetDesktopDisplayMode.md)
* [SDL_GetDisplayMode](SDL_GetDisplayMode.md)
* [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays.md)
* [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode.md)

----
[CategoryAPI](CategoryAPI.md)
