# SDL_SetGamepadLED

Update a gamepad's LED color.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_SetGamepadLED(SDL_Gamepad *gamepad, Uint8 red, Uint8 green, Uint8 blue);
```

## Function Parameters

|                              |             |                                 |
| ---------------------------- | ----------- | ------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | the gamepad to update.          |
| Uint8                        | **red**     | the intensity of the red LED.   |
| Uint8                        | **green**   | the intensity of the green LED. |
| Uint8                        | **blue**    | the intensity of the blue LED.  |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

An example of a joystick LED is the light on the back of a PlayStation 4's
DualShock 4 controller.

For gamepads with a single color LED, the maximum of the RGB values will be
used as the LED brightness.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

