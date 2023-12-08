###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetJoystick

Get the Joystick ID from a Game Controller.

## Syntax

```c
SDL_Joystick* SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);

```

## Function Parameters

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| **gamecontroller**     | the game controller object that you want to get a joystick from |

## Return Value

Returns a [SDL_Joystick](SDL_Joystick.md) object; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function will give you a [SDL_Joystick](SDL_Joystick.md) object, which
allows you to use the [SDL_Joystick](SDL_Joystick.md) functions with a
[SDL_GameController](SDL_GameController.md) object. This would be useful for
getting a joystick's position at any given time, even if it hasn't moved
(moving it would produce an event, which would have the axis' value).

The pointer returned is owned by the
[SDL_GameController](SDL_GameController.md). You should not call
[SDL_JoystickClose](SDL_JoystickClose.md)() on it, for example, since doing so
will likely cause SDL to crash.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
