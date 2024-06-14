###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowResizable

Set the user-resizable state of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_SetWindowResizable(SDL_Window *window, SDL_bool resizable);
```

## Function Parameters

|                            |               |                                                                             |
| -------------------------- | ------------- | --------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**    | the window of which to change the resizable state.                          |
| [SDL_bool](SDL_bool)       | **resizable** | [SDL_TRUE](SDL_TRUE) to allow resizing, [SDL_FALSE](SDL_FALSE) to disallow. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE) flag and allow/disallow user
resizing of the window. This is a no-op if the window's resizable state
already matches the requested state.

You can't change the resizable state of a fullscreen window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

