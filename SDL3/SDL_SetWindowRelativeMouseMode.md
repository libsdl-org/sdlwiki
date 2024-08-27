###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowRelativeMouseMode

Set relative mouse mode for a window.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_bool SDL_SetWindowRelativeMouseMode(SDL_Window *window, SDL_bool enabled);
```

## Function Parameters

|                            |             |                                                                                  |
| -------------------------- | ----------- | -------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**  | the window to change.                                                            |
| [SDL_bool](SDL_bool)       | **enabled** | [SDL_TRUE](SDL_TRUE) to enable relative mode, [SDL_FALSE](SDL_FALSE) to disable. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

While the window has focus and relative mouse mode is enabled, the cursor
is hidden, the mouse position is constrained to the window, and SDL will
report continuous relative mouse motion even if the mouse is at the edge of
the window.

This function will flush any pending mouse motion for this window.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetWindowRelativeMouseMode](SDL_GetWindowRelativeMouseMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

