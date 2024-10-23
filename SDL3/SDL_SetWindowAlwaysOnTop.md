###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowAlwaysOnTop

Set the window to always be above the others.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowAlwaysOnTop(SDL_Window *window, bool on_top);
```

## Function Parameters

|                            |            |                                                         |
| -------------------------- | ---------- | ------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window of which to change the always on top state.  |
| bool                       | **on_top** | true to set the window always on top, false to disable. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_ALWAYS_ON_TOP`](SDL_WINDOW_ALWAYS_ON_TOP) flag. This will
bring the window to the front and keep the window above the rest.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

