###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadFromInstanceID

Get the [SDL_Gamepad](SDL_Gamepad) associated with a joystick instance ID, if it has been opened.

## Syntax

```c
SDL_Gamepad* SDL_GetGamepadFromInstanceID(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                                         |
| ------------------- | --------------------------------------- |
| **instance_id**     | the joystick instance ID of the gamepad |

## Return Value

Returns an [SDL_Gamepad](SDL_Gamepad) on success or NULL on failure or if
it hasn't been opened yet; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

