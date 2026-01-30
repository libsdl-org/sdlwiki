# SDL_TryLockJoysticks

Locking for atomic access to the joystick API.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_TryLockJoysticks(void);
```

## Return Value

(bool) Returns true if the joysticks were successfully locked, false
otherwise.

## Remarks

The SDL joystick functions are thread-safe, however you can lock the
joysticks while processing to guarantee that the joystick list won't change
and joystick and gamepad events will not be delivered.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

