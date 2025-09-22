# SDL_UnlockJoysticks

Unlocking for atomic access to the joystick API.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
void SDL_UnlockJoysticks(void);
```

## Thread Safety

This should be called from the same thread that called
[SDL_LockJoysticks](SDL_LockJoysticks)().

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

