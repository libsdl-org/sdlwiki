###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGlobalMouseState

Query the platform for the asynchronous mouse button state and the desktop-relative platform-cursor position.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetGlobalMouseState(float *x, float *y);
```

## Function Parameters

|         |       |                                                                                                                  |
| ------- | ----- | ---------------------------------------------------------------------------------------------------------------- |
| float * | **x** | a pointer to receive the platform-cursor's x-position from the desktop's top left corner, can be NULL if unused. |
| float * | **y** | a pointer to receive the platform-cursor's y-position from the desktop's top left corner, can be NULL if unused. |

## Return Value

([SDL_MouseButtonFlags](SDL_MouseButtonFlags)) Returns a 32-bit bitmask of
the button state that can be bitwise-compared against the
[SDL_BUTTON_MASK](SDL_BUTTON_MASK)(X) macro.

## Remarks

This function immediately queries the platform for the most recent
asynchronous state, more costly than retrieving SDL's cached state in
[SDL_GetMouseState](SDL_GetMouseState)().

Passing non-NULL pointers to `x` or `y` will write the destination with
respective x or y coordinates relative to the desktop.

In Relative Mode, the platform-cursor's position usually contradicts the
SDL-cursor's position as manually calculated from
[SDL_GetMouseState](SDL_GetMouseState)() and
[SDL_GetWindowPosition](SDL_GetWindowPosition).

This function can be useful if you need to track the mouse outside of a
specific window and [SDL_CaptureMouse](SDL_CaptureMouse)() doesn't fit your
needs. For example, it could be useful if you need to track the mouse while
dragging a window, where coordinates relative to a window might not be in
sync at all times.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CaptureMouse](SDL_CaptureMouse)
- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

