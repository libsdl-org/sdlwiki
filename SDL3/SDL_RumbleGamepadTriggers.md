###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RumbleGamepadTriggers

Start a rumble effect in the gamepad's triggers.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_RumbleGamepadTriggers(SDL_Gamepad *gamepad, Uint16 left_rumble, Uint16 right_rumble, Uint32 duration_ms);
```

## Function Parameters

|                              |                  |                                                                    |
| ---------------------------- | ---------------- | ------------------------------------------------------------------ |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad**      | the gamepad to vibrate.                                            |
| Uint16                       | **left_rumble**  | the intensity of the left trigger rumble motor, from 0 to 0xFFFF.  |
| Uint16                       | **right_rumble** | the intensity of the right trigger rumble motor, from 0 to 0xFFFF. |
| Uint32                       | **duration_ms**  | the duration of the rumble effect, in milliseconds.                |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each call to this function cancels any previous trigger rumble effect, and
calling it with 0 intensity stops any rumbling.

Note that this is rumbling of the _triggers_ and not the gamepad as a
whole. This is currently only supported on Xbox One gamepads. If you want
the (more common) whole-gamepad rumble, use
[SDL_RumbleGamepad](SDL_RumbleGamepad)() instead.

This function requires you to process SDL events or call
[SDL_UpdateJoysticks](SDL_UpdateJoysticks)() to update rumble state.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_RumbleGamepad](SDL_RumbleGamepad)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

