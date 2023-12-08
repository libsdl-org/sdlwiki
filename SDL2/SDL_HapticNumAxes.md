###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticNumAxes

Get the number of haptic axes the device has.

## Syntax

```c
int SDL_HapticNumAxes(SDL_Haptic * haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic.md) device to query |

## Return Value

Returns the number of axes on success or a negative error code on failure;
call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The number of haptic axes might be useful if working with the
[SDL_HapticDirection](SDL_HapticDirection.md) effect.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
