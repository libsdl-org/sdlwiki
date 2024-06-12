###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayMode

Get information about a specific display mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetDisplayMode(int displayIndex, int modeIndex,
                   SDL_DisplayMode * mode);
```

## Function Parameters

|                                      |                  |                                                                                        |
| ------------------------------------ | ---------------- | -------------------------------------------------------------------------------------- |
| int                                  | **displayIndex** | the index of the display to query                                                      |
| int                                  | **modeIndex**    | the index of the display mode to query                                                 |
| [SDL_DisplayMode](SDL_DisplayMode) * | **mode**         | an [SDL_DisplayMode](SDL_DisplayMode) structure filled in with the mode at `modeIndex` |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The display modes are sorted in this priority:

- width -> largest to smallest
- height -> largest to smallest
- bits per pixel -> more colors to fewer colors
- packed pixel layout -> largest to smallest
- refresh rate -> highest to lowest

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumDisplayModes](SDL_GetNumDisplayModes)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

