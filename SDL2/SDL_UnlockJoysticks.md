###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnlockJoysticks

Unlocking for multi-threaded access to the joystick API

## Syntax

```c
void SDL_UnlockJoysticks(void) SDL_RELEASE(SDL_joystick_lock);

```

## Remarks

If you are using the joystick API or handling events from multiple threads
you should use these locking functions to protect access to the joysticks.

In particular, you are guaranteed that the joystick list won't change, so
the API functions that take a joystick index will be valid, and joystick
and game controller events will not be delivered.

## Version

This function is available since SDL 2.0.7.

----
[CategoryAPI](CategoryAPI.md)
