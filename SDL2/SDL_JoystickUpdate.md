###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickUpdate

Update the current state of the open joysticks.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
void SDL_JoystickUpdate(void);

```

## Remarks

This is called automatically by the event loop if any joystick events are
enabled.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_JoystickEventState](SDL_JoystickEventState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

