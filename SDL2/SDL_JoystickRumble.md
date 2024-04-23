###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickRumble

Start a rumble effect.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
int SDL_JoystickRumble(SDL_Joystick *joystick, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble, Uint32 duration_ms);

```

## Function Parameters

|                               |                                                                            |
| ----------------------------- | -------------------------------------------------------------------------- |
| **joystick**                  | The joystick to vibrate                                                    |
| **low_frequency_rumble**      | The intensity of the low frequency (left) rumble motor, from 0 to 0xFFFF   |
| **high_frequency_rumble**     | The intensity of the high frequency (right) rumble motor, from 0 to 0xFFFF |
| **duration_ms**               | The duration of the rumble effect, in milliseconds                         |

## Return Value

Returns 0, or -1 if rumble isn't supported on this joystick

## Remarks

Each call to this function cancels any previous rumble effect, and calling
it with 0 intensity stops any rumbling.

## Version

This function is available since SDL 2.0.9.

## Related Functions

* [SDL_JoystickHasRumble](SDL_JoystickHasRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


