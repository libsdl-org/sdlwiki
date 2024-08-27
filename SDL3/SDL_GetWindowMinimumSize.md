###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowMinimumSize

Get the minimum size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_GetWindowMinimumSize(SDL_Window *window, int *w, int *h);
```

## Function Parameters

|                            |            |                                                                         |
| -------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query.                                                    |
| int *                      | **w**      | a pointer filled in with the minimum width of the window, may be NULL.  |
| int *                      | **h**      | a pointer filled in with the minimum height of the window, may be NULL. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowMaximumSize](SDL_GetWindowMaximumSize)
- [SDL_SetWindowMinimumSize](SDL_SetWindowMinimumSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

