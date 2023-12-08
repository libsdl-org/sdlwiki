###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticOpenFromMouse

Try to open a haptic device from the current mouse.

## Syntax

```c
SDL_Haptic* SDL_HapticOpenFromMouse(void);

```

## Return Value

Returns the haptic device identifier or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticOpen](SDL_HapticOpen.md)
* [SDL_MouseIsHaptic](SDL_MouseIsHaptic.md)

----
[CategoryAPI](CategoryAPI.md)
