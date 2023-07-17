###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadType

Get the type of an opened gamepad.

## Syntax

```c
SDL_GamepadType SDL_GetGamepadType(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the gamepad type, or
[SDL_GAMEPAD_TYPE_UNKNOWN](SDL_GAMEPAD_TYPE_UNKNOWN) if it's not available.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadInstanceType](SDL_GetGamepadInstanceType)

----
[CategoryAPI](CategoryAPI)

