# SDL_GetGamepadConnectionState

Get the connection state of a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
SDL_JoystickConnectionState SDL_GetGamepadConnectionState(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                              |
| ---------------------------- | ----------- | ---------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | the gamepad object to query. |

## Return Value

([SDL_JoystickConnectionState](SDL_JoystickConnectionState)) Returns the
connection state on success or
[`SDL_JOYSTICK_CONNECTION_INVALID`](SDL_JOYSTICK_CONNECTION_INVALID) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

