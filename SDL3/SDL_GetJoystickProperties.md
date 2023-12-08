###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickProperties

Get the properties associated with a joystick.

## Syntax

```c
SDL_PropertiesID SDL_GetJoystickProperties(SDL_Joystick *joystick);

```

## Function Parameters

|                  |                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------- |
| **joystick**     | the [SDL_Joystick](SDL_Joystick.md) obtained from [SDL_OpenJoystick](SDL_OpenJoystick.md)() |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty.md)
* [SDL_SetProperty](SDL_SetProperty.md)

----
[CategoryAPI](CategoryAPI.md)
