###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowAspectRatio

Get the size of a window's client area.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_GetWindowAspectRatio(SDL_Window *window, float *min_aspect, float *max_aspect);
```

## Function Parameters

|                            |                |                                                                               |
| -------------------------- | -------------- | ----------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**     | the window to query the width and height from.                                |
| float *                    | **min_aspect** | a pointer filled in with the minimum aspect ratio of the window, may be NULL. |
| float *                    | **max_aspect** | a pointer filled in with the maximum aspect ratio of the window, may be NULL. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowAspectRatio](SDL_SetWindowAspectRatio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

