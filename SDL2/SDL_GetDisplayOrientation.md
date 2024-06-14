###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayOrientation

Get the orientation of a display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_DisplayOrientation SDL_GetDisplayOrientation(int displayIndex);
```

## Function Parameters

|     |                  |                                    |
| --- | ---------------- | ---------------------------------- |
| int | **displayIndex** | the index of the display to query. |

## Return Value

([SDL_DisplayOrientation](SDL_DisplayOrientation)) Returns The
[SDL_DisplayOrientation](SDL_DisplayOrientation) enum value of the display,
or [`SDL_ORIENTATION_UNKNOWN`](SDL_ORIENTATION_UNKNOWN) if it isn't
available.

## Version

This function is available since SDL 2.0.9.

## See Also

- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

