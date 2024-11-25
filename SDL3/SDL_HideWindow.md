###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HideWindow

Hide a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_HideWindow(SDL_Window *window);
```

## Function Parameters

|                            |            |                     |
| -------------------------- | ---------- | ------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to hide. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_ShowWindow](SDL_ShowWindow)
- [SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

