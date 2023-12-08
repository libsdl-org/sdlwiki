###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetTouchpadFinger

Get the current state of a finger on a touchpad on a game controller.

## Syntax

```c
int SDL_GameControllerGetTouchpadFinger(SDL_GameController *gamecontroller, int touchpad, int finger, Uint8 *state, float *x, float *y, float *pressure);

```

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
