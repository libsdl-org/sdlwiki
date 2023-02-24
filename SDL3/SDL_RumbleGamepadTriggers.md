###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RumbleGamepadTriggers

Start a rumble effect in the gamepad's triggers.

## Syntax

```c
int SDL_RumbleGamepadTriggers(SDL_Gamepad *gamepad, Uint16 left_rumble, Uint16 right_rumble, Uint32 duration_ms);

```

## Function Parameters

|                      |                                                                   |
| -------------------- | ----------------------------------------------------------------- |
| **gamepad**          | The gamepad to vibrate                                            |
| **left_rumble**      | The intensity of the left trigger rumble motor, from 0 to 0xFFFF  |
| **right_rumble**     | The intensity of the right trigger rumble motor, from 0 to 0xFFFF |
| **duration_ms**      | The duration of the rumble effect, in milliseconds                |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each call to this function cancels any previous trigger rumble effect, and
calling it with 0 intensity stops any rumbling.

Note that this is rumbling of the _triggers_ and not the gamepad as a
whole. This is currently only supported on Xbox One gamepads. If you want
the (more common) whole-gamepad rumble, use
[SDL_RumbleGamepad](SDL_RumbleGamepad)() instead.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GamepadHasRumbleTriggers](SDL_GamepadHasRumbleTriggers)

----
[CategoryAPI](CategoryAPI)

