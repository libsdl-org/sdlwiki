# SDL_WarpMouseInWindow

Move the mouse cursor to the given position within the window.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
void SDL_WarpMouseInWindow(SDL_Window *window,
                       float x, float y);
```

## Function Parameters

|                            |            |                                                                         |
| -------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to move the mouse into, or NULL for the current mouse focus. |
| float                      | **x**      | the x coordinate within the window.                                     |
| float                      | **y**      | the y coordinate within the window.                                     |

## Remarks

This function generates a mouse motion event if relative mode is not
enabled. If relative mode is enabled, you can force mouse events for the
warp by setting the
[SDL_HINT_MOUSE_RELATIVE_WARP_MOTION](SDL_HINT_MOUSE_RELATIVE_WARP_MOTION)
hint.

Note that this function will appear to succeed, but not actually move the
mouse when used over Microsoft Remote Desktop.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_WarpMouseGlobal](SDL_WarpMouseGlobal)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

