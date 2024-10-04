###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowMinimumSize

Set the minimum size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMinimumSize(SDL_Window *window, int min_w, int min_h);
```

## Function Parameters

|                            |            |                                                      |
| -------------------------- | ---------- | ---------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                                |
| int                        | **min_w**  | the minimum width of the window, or 0 for no limit.  |
| int                        | **min_h**  | the minimum height of the window, or 0 for no limit. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowMinimumSize](SDL_GetWindowMinimumSize)
- [SDL_SetWindowMaximumSize](SDL_SetWindowMaximumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

