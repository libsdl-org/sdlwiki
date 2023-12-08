###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickFromInstanceID

Get the [SDL_Joystick](SDL_Joystick.md) associated with an instance id.

## Syntax

```c
SDL_Joystick* SDL_JoystickFromInstanceID(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                                                             |
| ------------------- | ----------------------------------------------------------- |
| **instance_id**     | the instance id to get the [SDL_Joystick](SDL_Joystick.md) for |

## Return Value

Returns an [SDL_Joystick](SDL_Joystick.md) on success or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.4.

----
[CategoryAPI](CategoryAPI.md)
