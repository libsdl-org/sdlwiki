###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsJoystickVirtual

Query whether or not a joystick is virtual.

## Syntax

```c
SDL_bool SDL_IsJoystickVirtual(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the joystick is virtual,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

