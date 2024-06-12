###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowTitle

Get the title of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
const char* SDL_GetWindowTitle(SDL_Window * window);
```

## Function Parameters

|                            |            |                     |
| -------------------------- | ---------- | ------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query |

## Return Value

(const char *) Returns the title of the window in UTF-8 format or "" if
there is no title.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetWindowTitle](SDL_SetWindowTitle)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

