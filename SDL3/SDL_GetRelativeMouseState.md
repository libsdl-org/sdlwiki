###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRelativeMouseState

Retrieve the relative state of the mouse.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetRelativeMouseState(float *x, float *y);
```

## Function Parameters

|           |                                                                   |
| --------- | ----------------------------------------------------------------- |
| **x**     | a pointer filled with the last recorded x coordinate of the mouse |
| **y**     | a pointer filled with the last recorded y coordinate of the mouse |

## Return Value

Returns a 32-bit button bitmask of the relative button state.

## Remarks

The current button state is returned as a button bitmask, which can be
tested using the `SDL_BUTTON(X)` macros (where `X` is generally 1 for the
left, 2 for middle, 3 for the right button), and `x` and `y` are set to the
mouse deltas since the last call to
[SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)() or since event
initialization. You can pass NULL for either `x` or `y`.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetMouseState](SDL_GetMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

