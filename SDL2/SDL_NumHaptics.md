###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_NumHaptics

Count the number of haptic devices attached to the system.

## Syntax

```c
int SDL_NumHaptics(void);

```

## Return Value

Returns the number of haptic devices detected on the system or a negative
error code on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticName](SDL_HapticName.md)

----
[CategoryAPI](CategoryAPI.md)
