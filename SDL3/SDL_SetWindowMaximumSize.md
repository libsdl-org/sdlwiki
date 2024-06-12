###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowMaximumSize

Set the maximum size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowMaximumSize(SDL_Window *window, int max_w, int max_h);
```

## Function Parameters

|                            |            |                                                     |
| -------------------------- | ---------- | --------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change                                |
| int                        | **max_w**  | the maximum width of the window, or 0 for no limit  |
| int                        | **max_h**  | the maximum height of the window, or 0 for no limit |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

