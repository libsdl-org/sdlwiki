###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadJoystick

Get the underlying joystick from a gamepad 

## Syntax

```c
SDL_Joystick* SDL_GetGamepadJoystick(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                         |
| --------------- | ------------------------------------------------------- |
| **gamepad**     | the gamepad object that you want to get a joystick from |

## Return Value

Returns an [SDL_Joystick](SDL_Joystick) object; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function will give you a [SDL_Joystick](SDL_Joystick) object, which
allows you to use the [SDL_Joystick](SDL_Joystick) functions with a
[SDL_Gamepad](SDL_Gamepad) object. This would be useful for getting a
joystick's position at any given time, even if it hasn't moved (moving it
would produce an event, which would have the axis' value).

The pointer returned is owned by the [SDL_Gamepad](SDL_Gamepad). You should
not call [SDL_CloseJoystick](SDL_CloseJoystick)() on it, for example, since
doing so will likely cause SDL to crash.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

