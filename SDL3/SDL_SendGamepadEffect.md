###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SendGamepadEffect

Send a gamepad specific effect packet 

## Syntax

```c
int SDL_SendGamepadEffect(SDL_Gamepad *gamepad, const void *data, int size);

```

## Function Parameters

|                 |                                             |
| --------------- | ------------------------------------------- |
| **gamepad**     | The gamepad to affect                       |
| **data**        | The data to send to the gamepad             |
| **size**        | The size of the data to send to the gamepad |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

