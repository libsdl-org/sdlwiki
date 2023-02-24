###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadButton

Get the current state of a button on a gamepad.

## Syntax

```c
Uint8 SDL_GetGamepadButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);

```

## Function Parameters

|                 |                                                                           |
| --------------- | ------------------------------------------------------------------------- |
| **gamepad**     | a gamepad                                                                 |
| **button**      | a button index (one of the [SDL_GamepadButton](SDL_GamepadButton) values) |

## Return Value

Returns 1 for pressed state or 0 for not pressed state or error; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadAxis](SDL_GetGamepadAxis)

----
[CategoryAPI](CategoryAPI)

