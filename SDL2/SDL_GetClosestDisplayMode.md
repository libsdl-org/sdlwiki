###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetClosestDisplayMode

Get the closest match to the requested display mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_DisplayMode * SDL_GetClosestDisplayMode(int displayIndex, const SDL_DisplayMode * mode, SDL_DisplayMode * closest);

```

## Function Parameters

|                      |                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| **displayIndex**     | the index of the display to query                                                                               |
| **mode**             | an [SDL_DisplayMode](SDL_DisplayMode) structure containing the desired display mode                             |
| **closest**          | an [SDL_DisplayMode](SDL_DisplayMode) structure filled in with the closest match of the available display modes |

## Return Value

Returns the passed in value `closest` or NULL if no matching video mode was
available; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The available display modes are scanned and `closest` is filled in with the
closest mode matching the requested mode and returned. The mode format and
refresh rate default to the desktop mode if they are set to 0. The modes
are scanned with size being first priority, format being second priority,
and finally checking the refresh rate. If all the available modes are too
small, then NULL is returned.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetDisplayMode](SDL_GetDisplayMode)
- [SDL_GetNumDisplayModes](SDL_GetNumDisplayModes)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

