###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LockJoysticks

Locking for atomic access to the joystick API 

## Syntax

```c
void SDL_LockJoysticks(void) SDL_ACQUIRE(SDL_joystick_lock);

```

## Remarks

The SDL joystick functions are thread-safe, however you can lock the
joysticks while processing to guarantee that the joystick list won't change
and joystick and gamepad events will not be delivered.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

