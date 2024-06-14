###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerGetJoystick

Get the Joystick ID from a Game Controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
SDL_Joystick* SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);
```

## Function Parameters

|                                            |                    |                                                                  |
| ------------------------------------------ | ------------------ | ---------------------------------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | the game controller object that you want to get a joystick from. |

## Return Value

([SDL_Joystick](SDL_Joystick) *) Returns a [SDL_Joystick](SDL_Joystick)
object; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function will give you a [SDL_Joystick](SDL_Joystick) object, which
allows you to use the [SDL_Joystick](SDL_Joystick) functions with a
[SDL_GameController](SDL_GameController) object. This would be useful for
getting a joystick's position at any given time, even if it hasn't moved
(moving it would produce an event, which would have the axis' value).

The pointer returned is owned by the
[SDL_GameController](SDL_GameController). You should not call
[SDL_JoystickClose](SDL_JoystickClose)() on it, for example, since doing so
will likely cause SDL to crash.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

