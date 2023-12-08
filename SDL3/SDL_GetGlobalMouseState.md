###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetGlobalMouseState

Get the current state of the mouse in relation to the desktop.

## Syntax

```c
Uint32 SDL_GetGlobalMouseState(float *x, float *y);

```

## Function Parameters

|           |                                                                         |
| --------- | ----------------------------------------------------------------------- |
| **x**     | filled in with the current X coord relative to the desktop; can be NULL |
| **y**     | filled in with the current Y coord relative to the desktop; can be NULL |

## Return Value

Returns the current button state as a bitmask which can be tested using the
[SDL_BUTTON](SDL_BUTTON.md)(X) macros.

## Remarks

This works similarly to [SDL_GetMouseState](SDL_GetMouseState.md)(), but the
coordinates will be reported relative to the top-left of the desktop. This
can be useful if you need to track the mouse outside of a specific window
and [SDL_CaptureMouse](SDL_CaptureMouse.md)() doesn't fit your needs. For
example, it could be useful if you need to track the mouse while dragging a
window, where coordinates relative to a window might not be in sync at all
times.

Note: [SDL_GetMouseState](SDL_GetMouseState.md)() returns the mouse position
as SDL understands it from the last pump of the event queue. This function,
however, queries the OS for the current mouse position, and as such, might
be a slightly less efficient function. Unless you know what you're doing
and have a good reason to use this function, you probably want
[SDL_GetMouseState](SDL_GetMouseState.md)() instead.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CaptureMouse](SDL_CaptureMouse.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMouse](CategoryMouse.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
