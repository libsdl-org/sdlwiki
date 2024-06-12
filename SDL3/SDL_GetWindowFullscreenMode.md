###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowFullscreenMode

Query the display mode to use when a window is visible at fullscreen.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
const SDL_DisplayMode* SDL_GetWindowFullscreenMode(SDL_Window *window);
```

## Function Parameters

|                            |            |                     |
| -------------------------- | ---------- | ------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query |

## Return Value

(const [SDL_DisplayMode](SDL_DisplayMode) *) Returns a pointer to the
exclusive fullscreen mode to use or NULL for borderless fullscreen desktop
mode

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)
- [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

