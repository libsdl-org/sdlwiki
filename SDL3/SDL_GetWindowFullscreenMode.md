# SDL_GetWindowFullscreenMode

Query the display mode to use when a window is visible at fullscreen.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_DisplayMode * SDL_GetWindowFullscreenMode(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

(const [SDL_DisplayMode](SDL_DisplayMode) *) Returns a pointer to the
exclusive fullscreen mode to use or NULL for borderless fullscreen desktop
mode.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
- [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

