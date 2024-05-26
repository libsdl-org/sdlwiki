###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGlobalMouseState

Get the current state of the mouse in relation to the desktop.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseButtonFlags SDL_GetGlobalMouseState(float *x, float *y);

```

## Function Parameters

|           |                                                                         |
| --------- | ----------------------------------------------------------------------- |
| **x**     | filled in with the current X coord relative to the desktop; can be NULL |
| **y**     | filled in with the current Y coord relative to the desktop; can be NULL |

## Return Value

Returns the current button state as a bitmask which can be tested using the
[SDL_BUTTON](SDL_BUTTON)(X) macros.

## Remarks

This works similarly to [SDL_GetMouseState](SDL_GetMouseState)(), but the
coordinates will be reported relative to the top-left of the desktop. This
can be useful if you need to track the mouse outside of a specific window
and [SDL_CaptureMouse](SDL_CaptureMouse)() doesn't fit your needs. For
example, it could be useful if you need to track the mouse while dragging a
window, where coordinates relative to a window might not be in sync at all
times.

Note: [SDL_GetMouseState](SDL_GetMouseState)() returns the mouse position
as SDL understands it from the last pump of the event queue. This function,
however, queries the OS for the current mouse position, and as such, might
be a slightly less efficient function. Unless you know what you're doing
and have a good reason to use this function, you probably want
[SDL_GetMouseState](SDL_GetMouseState)() instead.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CaptureMouse](SDL_CaptureMouse)
- [SDL_GetMouseState](SDL_GetMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

