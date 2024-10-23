###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetJoystickType

Get the type of an opened joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_JoystickType SDL_GetJoystickType(SDL_Joystick *joystick);
```

## Function Parameters

|                                |              |                                                                                        |
| ------------------------------ | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the [SDL_Joystick](SDL_Joystick) obtained from [SDL_OpenJoystick](SDL_OpenJoystick)(). |

## Return Value

([SDL_JoystickType](SDL_JoystickType)) Returns the
[SDL_JoystickType](SDL_JoystickType) of the selected joystick.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetJoystickTypeForID](SDL_GetJoystickTypeForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

