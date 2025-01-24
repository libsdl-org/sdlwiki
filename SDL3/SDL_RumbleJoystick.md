# SDL_RumbleJoystick

Start a rumble effect.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_RumbleJoystick(SDL_Joystick *joystick, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble, Uint32 duration_ms);
```

## Function Parameters

|                                |                           |                                                                             |
| ------------------------------ | ------------------------- | --------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick**              | the joystick to vibrate.                                                    |
| [Uint16](Uint16)               | **low_frequency_rumble**  | the intensity of the low frequency (left) rumble motor, from 0 to 0xFFFF.   |
| [Uint16](Uint16)               | **high_frequency_rumble** | the intensity of the high frequency (right) rumble motor, from 0 to 0xFFFF. |
| [Uint32](Uint32)               | **duration_ms**           | the duration of the rumble effect, in milliseconds.                         |

## Return Value

(bool) Returns true, or false if rumble isn't supported on this joystick.

## Remarks

Each call to this function cancels any previous rumble effect, and calling
it with 0 intensity stops any rumbling.

This function requires you to process SDL events or call
[SDL_UpdateJoysticks](SDL_UpdateJoysticks)() to update rumble state.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

