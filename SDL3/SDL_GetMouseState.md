# SDL_GetMouseState

Query SDL's cache for the synchronous mouse button state and the window-relative SDL-cursor position.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetMouseState(float *x, float *y);
```

## Function Parameters

|         |       |                                                                                                                    |
| ------- | ----- | ------------------------------------------------------------------------------------------------------------------ |
| float * | **x** | a pointer to receive the SDL-cursor's x-position from the focused window's top left corner, can be NULL if unused. |
| float * | **y** | a pointer to receive the SDL-cursor's y-position from the focused window's top left corner, can be NULL if unused. |

## Return Value

([SDL_MouseButtonFlags](SDL_MouseButtonFlags)) Returns a 32-bit bitmask of
the button state that can be bitwise-compared against the
[SDL_BUTTON_MASK](SDL_BUTTON_MASK)(X) macro.

## Remarks

This function returns the cached synchronous state as SDL understands it
from the last pump of the event queue.

To query the platform for immediate asynchronous state, use
[SDL_GetGlobalMouseState](SDL_GetGlobalMouseState).

Passing non-NULL pointers to `x` or `y` will write the destination with
respective x or y coordinates relative to the focused window.

In Relative Mode, the SDL-cursor's position usually contradicts the
platform-cursor's position as manually calculated from
[SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)() and
[SDL_GetWindowPosition](SDL_GetWindowPosition).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)
- [SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

