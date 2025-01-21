###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowBordered

Set the border state of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowBordered(SDL_Window *window, bool bordered);
```

## Function Parameters

|                            |              |                                                 |
| -------------------------- | ------------ | ----------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**   | the window of which to change the border state. |
| bool                       | **bordered** | false to remove border, true to add border.     |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS) flag and add or remove the
border from the actual window. This is a no-op if the window's border
already matches the requested state.

You can't change the border state of a fullscreen window.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

