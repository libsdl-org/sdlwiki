###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticOpen

Open a haptic device for use.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
SDL_Haptic* SDL_HapticOpen(int device_index);

```

## Function Parameters

|                      |                             |
| -------------------- | --------------------------- |
| **device_index**     | index of the device to open |

## Return Value

Returns the device identifier or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The index passed as an argument refers to the N'th haptic device on this
system.

When opening a haptic device, its gain will be set to maximum and
autocenter will be disabled. To modify these values use
[SDL_HapticSetGain](SDL_HapticSetGain)() and
[SDL_HapticSetAutocenter](SDL_HapticSetAutocenter)().

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_HapticClose](SDL_HapticClose)
* [SDL_HapticIndex](SDL_HapticIndex)
* [SDL_HapticOpenFromJoystick](SDL_HapticOpenFromJoystick)
* [SDL_HapticOpenFromMouse](SDL_HapticOpenFromMouse)
* [SDL_HapticPause](SDL_HapticPause)
* [SDL_HapticSetAutocenter](SDL_HapticSetAutocenter)
* [SDL_HapticSetGain](SDL_HapticSetGain)
* [SDL_HapticStopAll](SDL_HapticStopAll)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

