###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_NumHaptics

Count the number of haptic devices attached to the system.

## Syntax

```c
int SDL_NumHaptics(void);

```

## Return Value

Returns the number of haptic devices detected on the system or a negative
error code on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticName](SDL_HapticName)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


