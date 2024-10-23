###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindowMinimumSize

Get the minimum size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetWindowMinimumSize(SDL_Window *window, int *w, int *h);
```

## Function Parameters

|                            |            |                                                                         |
| -------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query.                                                    |
| int *                      | **w**      | a pointer filled in with the minimum width of the window, may be NULL.  |
| int *                      | **h**      | a pointer filled in with the minimum height of the window, may be NULL. |

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

