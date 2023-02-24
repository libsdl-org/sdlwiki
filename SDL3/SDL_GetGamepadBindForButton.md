###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadBindForButton

Get the SDL joystick layer binding for a gamepad button mapping.

## Syntax

```c
SDL_GamepadBinding SDL_GetGamepadBindForButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **gamepad**     | a gamepad                                                              |
| **button**      | an button enum value (an [SDL_GamepadButton](SDL_GamepadButton) value) |

## Return Value

Returns a [SDL_GamepadBinding](SDL_GamepadBinding) describing the bind. On
failure (like the given Controller button doesn't exist on the device), its
`.bindType` will be
[`SDL_GAMEPAD_BINDTYPE_NONE`](SDL_GAMEPAD_BINDTYPE_NONE).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadBindForAxis](SDL_GetGamepadBindForAxis)

----
[CategoryAPI](CategoryAPI)

