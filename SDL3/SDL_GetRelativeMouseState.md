###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRelativeMouseState

Query SDL's cache for the synchronous mouse button state and accumulated mouse delta since last call.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetRelativeMouseState(float *x, float *y);
```

## Function Parameters

|         |       |                                                                                            |
| ------- | ----- | ------------------------------------------------------------------------------------------ |
| float * | **x** | a pointer to receive the x mouse delta accumulated since last call, can be NULL if unused. |
| float * | **y** | a pointer to receive the y mouse delta accumulated since last call, can be NULL if unused. |

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
respective x or y deltas accumulated since the last call to this function
(or since event initialization).

This function is useful for reducing overhead by processing relative mouse
inputs in one go per-frame instead of individually per-event, at the
expense of losing the order between events within the frame (e.g. quickly
pressing and releasing a button within the same frame).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

