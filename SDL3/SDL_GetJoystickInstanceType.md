###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickInstanceType

Get the type of a joystick, if available.

## Syntax

```c
SDL_JoystickType SDL_GetJoystickInstanceType(SDL_JoystickID instance_id);

```

## Function Parameters

|                     |                          |
| ------------------- | ------------------------ |
| **instance_id**     | the joystick instance ID |

## Return Value

Returns the [SDL_JoystickType](SDL_JoystickType) of the selected joystick.
If called on an invalid index, this function returns
[`SDL_JOYSTICK_TYPE_UNKNOWN`](SDL_JOYSTICK_TYPE_UNKNOWN)

## Remarks

This can be called before any joysticks are opened.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

