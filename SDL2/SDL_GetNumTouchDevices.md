###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumTouchDevices

Get the number of registered touch devices.

## Syntax

```c
int SDL_GetNumTouchDevices(void);

```

## Return Value

Returns the number of registered touch devices.

## Remarks

On some platforms SDL first sees the touch device if it was actually used.
Therefore [SDL_GetNumTouchDevices](SDL_GetNumTouchDevices.md)() may return 0
although devices are available. After using all devices at least once the
number will be correct.

This was fixed for Android in SDL 2.0.1.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetTouchDevice](SDL_GetTouchDevice.md)

----
[CategoryAPI](CategoryAPI.md)
