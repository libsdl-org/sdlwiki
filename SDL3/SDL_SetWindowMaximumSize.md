###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowMaximumSize

Set the maximum size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowMaximumSize(SDL_Window *window, int max_w, int max_h);
```

## Function Parameters

|                            |            |                                                      |
| -------------------------- | ---------- | ---------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                                |
| int                        | **max_w**  | the maximum width of the window, or 0 for no limit.  |
| int                        | **max_h**  | the maximum height of the window, or 0 for no limit. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

