###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SendJoystickEffect

Send a joystick specific effect packet 

## Syntax

```c
int SDL_SendJoystickEffect(SDL_Joystick *joystick, const void *data, int size);

```

## Function Parameters

|                  |                                              |
| ---------------- | -------------------------------------------- |
| **joystick**     | The joystick to affect                       |
| **data**         | The data to send to the joystick             |
| **size**         | The size of the data to send to the joystick |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

