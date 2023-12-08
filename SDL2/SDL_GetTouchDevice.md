###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetTouchDevice

Get the touch ID with the given index.

## Syntax

```c
SDL_TouchID SDL_GetTouchDevice(int index);

```

## Function Parameters

|               |                        |
| ------------- | ---------------------- |
| **index**     | the touch device index |

## Return Value

Returns the touch ID with the given index on success or 0 if the index is
invalid; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetNumTouchDevices](SDL_GetNumTouchDevices.md)

----
[CategoryAPI](CategoryAPI.md)
