# SDL_SendJoystickEffect

Send a joystick specific effect packet.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
bool SDL_SendJoystickEffect(SDL_Joystick *joystick, const void *data, int size);
```

## Function Parameters

|                                |              |                                               |
| ------------------------------ | ------------ | --------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the joystick to affect.                       |
| const void *                   | **data**     | the data to send to the joystick.             |
| int                            | **size**     | the size of the data to send to the joystick. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

