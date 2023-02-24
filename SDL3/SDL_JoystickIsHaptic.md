###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_JoystickIsHaptic

Query if a joystick has haptic features.

## Syntax

```c
int SDL_JoystickIsHaptic(SDL_Joystick * joystick);

```

## Function Parameters

|                  |                                                                  |
| ---------------- | ---------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to test for haptic capabilities |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the joystick is haptic,
[SDL_FALSE](SDL_FALSE) if it isn't, or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HapticOpenFromJoystick](SDL_HapticOpenFromJoystick)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


