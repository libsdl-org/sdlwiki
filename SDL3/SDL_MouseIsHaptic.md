###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_MouseIsHaptic

Query whether or not the current mouse has haptic capabilities.

## Syntax

```c
int SDL_MouseIsHaptic(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the mouse is haptic or
[SDL_FALSE](SDL_FALSE.md) if it isn't.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticOpenFromMouse](SDL_HapticOpenFromMouse.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
