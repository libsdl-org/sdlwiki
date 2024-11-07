###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGlobalMouseState

Query the platform for the asynchronous mouse button state and the desktop-relative cursor position.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetGlobalMouseState(float *x, float *y);
```

## Function Parameters

|         |       |                                                                                                         |
| ------- | ----- | ------------------------------------------------------------------------------------------------------- |
| float * | **x** | a pointer to receive the cursor's x-position from the desktop's top left corner, can be NULL if unused. |
| float * | **y** | a pointer to receive the cursor's y-position from the desktop's top left corner, can be NULL if unused. |

## Return Value

([SDL_MouseButtonFlags](SDL_MouseButtonFlags)) a 32-bit bitmask of the button state that can be bitwise-compared against the [SDL_BUTTON_MASK](SDL_BUTTON_MASK)(X) macro.

## Remarks

This function immediately queries the platform for the most recent asynchronous state, which is slower than the cached state of [SDL_GetMouseState](SDL_GetMouseState)().

Passing non-NULL pointers to `x` or `y` will write the destination with respective x or y cursor position relative to the desktop as reported by the platform.

In Relative Mode, the reported position usually contradict what you would manually calculated from [SDL_GetMouseState](SDL_GetMouseState)() and [SDL_GetWindowPosition](SDL_GetWindowPosition).

This function can be useful if you need to track the mouse outside of a specific window
and [SDL_CaptureMouse](SDL_CaptureMouse)() doesn't fit your needs. For
example, it could be useful if you need to track the mouse while dragging a
window, where coordinates relative to a window might not be in sync at all
times.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_CaptureMouse](SDL_CaptureMouse)
- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

