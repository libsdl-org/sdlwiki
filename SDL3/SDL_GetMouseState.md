###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetMouseState

Query SDL's internal buffer for the synchronous mouse button state and the window-relative cursor position.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetMouseState(float *x, float *y);
```

## Function Parameters

|         |       |                                                                                                                |
| ------- | ----- | -------------------------------------------------------------------------------------------------------------- |
| float * | **x** | a pointer to receive the cursor's x-position from the focused window's top left corner, can be NULL if unused. |
| float * | **y** | a pointer to receive the cursor's y-position from the focused window's top left corner, can be NULL if unused. |

## Return Value

([SDL_MouseButtonFlags](SDL_MouseButtonFlags)) a 32-bit bitmask of the button state.

## Remarks

This function returns the buffered synchronous state as SDL understands it from the last pump of the event queue. 

To query the platform for immediate asynchronous state, use [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState).

The button bitmask can be bitwise-compared against the [SDL_BUTTON_MASK](SDL_BUTTON_MASK)(X) macro (where `X` is generally 1 for the left, 2 for middle, 3 for the right button).

Passing non-NULL pointers to `x` or `y` will write the destination with respective x or y cursor position relative to the focused window.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)
- [SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

