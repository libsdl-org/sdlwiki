###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowSizeInPixels

Get the size of a window in pixels.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_GetWindowSizeInPixels(SDL_Window * window,
                           int *w, int *h);
```

## Function Parameters

|                            |            |                                                                     |
| -------------------------- | ---------- | ------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window from which the drawable size should be queried           |
| int *                      | **w**      | a pointer to variable for storing the width in pixels, may be NULL  |
| int *                      | **h**      | a pointer to variable for storing the height in pixels, may be NULL |

## Remarks

This may differ from [SDL_GetWindowSize](SDL_GetWindowSize)() if we're
rendering to a high-DPI drawable, i.e. the window was created with
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) on a platform with
high-DPI support (Apple calls this "Retina"), and not disabled by the
[`SDL_HINT_VIDEO_HIGHDPI_DISABLED`](SDL_HINT_VIDEO_HIGHDPI_DISABLED) hint.

## Version

This function is available since SDL 2.26.0.

## See Also

- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_GetWindowSize](SDL_GetWindowSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

