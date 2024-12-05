###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowRelativeMouseMode

Set relative mouse mode for a window.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_SetWindowRelativeMouseMode(SDL_Window *window, bool enabled);
```

## Function Parameters

|                            |             |                                                 |
| -------------------------- | ----------- | ----------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**  | the window to change.                           |
| bool                       | **enabled** | true to enable relative mode, false to disable. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

While the window has focus and relative mouse mode is enabled, the cursor
is hidden, the mouse position is constrained to the window, and SDL will
report continuous relative mouse motion even if the mouse is at the edge of
the window.

This function will flush any pending mouse motion for this window.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetWindowRelativeMouseMode](SDL_GetWindowRelativeMouseMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

