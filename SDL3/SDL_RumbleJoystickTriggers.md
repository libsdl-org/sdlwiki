###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RumbleJoystickTriggers

Start a rumble effect in the joystick's triggers 

## Syntax

```c
int SDL_RumbleJoystickTriggers(SDL_Joystick *joystick, Uint16 left_rumble, Uint16 right_rumble, Uint32 duration_ms);

```

## Function Parameters

|                      |                                                                   |
| -------------------- | ----------------------------------------------------------------- |
| **joystick**         | The joystick to vibrate                                           |
| **left_rumble**      | The intensity of the left trigger rumble motor, from 0 to 0xFFFF  |
| **right_rumble**     | The intensity of the right trigger rumble motor, from 0 to 0xFFFF |
| **duration_ms**      | The duration of the rumble effect, in milliseconds                |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Each call to this function cancels any previous trigger rumble effect, and
calling it with 0 intensity stops any rumbling.

Note that this is rumbling of the _triggers_ and not the game controller as
a whole. This is currently only supported on Xbox One controllers. If you
want the (more common) whole-controller rumble, use
[SDL_RumbleJoystick](SDL_RumbleJoystick)() instead.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_JoystickHasRumbleTriggers](SDL_JoystickHasRumbleTriggers)

----
[CategoryAPI](CategoryAPI)

