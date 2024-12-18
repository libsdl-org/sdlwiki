###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_UpdateJoysticks

Update the current state of the open joysticks.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
void SDL_UpdateJoysticks(void);
```

## Remarks

This is called automatically by the event loop if any joystick events are
enabled.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

