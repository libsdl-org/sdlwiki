###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticRumblePlay

Run a simple rumble effect on a haptic device.

## Syntax

```c
int SDL_HapticRumblePlay(SDL_Haptic * haptic, float strength, Uint32 length );

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **haptic**       | the haptic device to play the rumble effect on      |
| **strength**     | strength of the rumble to play as a 0-1 float value |
| **length**       | length of the rumble to play in milliseconds        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticRumbleInit](SDL_HapticRumbleInit.md)
* [SDL_HapticRumbleStop](SDL_HapticRumbleStop.md)
* [SDL_HapticRumbleSupported](SDL_HapticRumbleSupported.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryForceFeedback](CategoryForceFeedback.md), [CategoryDraft](CategoryDraft.md)
