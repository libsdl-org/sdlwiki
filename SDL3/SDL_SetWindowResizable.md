# SDL_SetWindowResizable

Set the user-resizable state of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowResizable(SDL_Window *window, bool resizable);
```

## Function Parameters

|                            |               |                                                    |
| -------------------------- | ------------- | -------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**    | the window of which to change the resizable state. |
| bool                       | **resizable** | true to allow resizing, false to disallow.         |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE) flag and allow/disallow user
resizing of the window. This is a no-op if the window's resizable state
already matches the requested state.

You can't change the resizable state of a fullscreen window.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowFlags](SDL_GetWindowFlags)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

