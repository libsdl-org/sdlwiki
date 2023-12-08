###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_MouseIsHaptic

Query whether or not the current mouse has haptic capabilities.

## Syntax

```c
int SDL_MouseIsHaptic(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the mouse is haptic or
[SDL_FALSE](SDL_FALSE.md) if it isn't.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpenFromMouse](SDL_HapticOpenFromMouse.md)

----
[CategoryAPI](CategoryAPI.md)
