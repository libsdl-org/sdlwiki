###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticOpenFromJoystick

Open a haptic device for use from a joystick device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Haptic* SDL_HapticOpenFromJoystick(SDL_Joystick *
                                       joystick);

```

## Function Parameters

|                  |                                                                 |
| ---------------- | --------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick) to create a haptic device from |

## Return Value

Returns a valid haptic device identifier on success or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

You must still close the haptic device separately. It will not be closed
with the joystick.

When opened from a joystick you should first close the haptic device before
closing the joystick device. If not, on some implementations the haptic
device will also get unallocated and you'll be unable to use force feedback
on that device.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HapticClose](SDL_HapticClose)
* [SDL_HapticOpen](SDL_HapticOpen)
* [SDL_JoystickIsHaptic](SDL_JoystickIsHaptic)

----
[CategoryAPI](CategoryAPI)

