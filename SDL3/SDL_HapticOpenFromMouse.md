###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticOpenFromMouse

Try to open a haptic device from the current mouse.

## Syntax

```c
SDL_Haptic* SDL_HapticOpenFromMouse(void);

```

## Return Value

Returns the haptic device identifier or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticOpen](SDL_HapticOpen.md)
* [SDL_MouseIsHaptic](SDL_MouseIsHaptic.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
