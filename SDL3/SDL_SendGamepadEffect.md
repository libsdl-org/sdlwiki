###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SendGamepadEffect

Send a gamepad specific effect packet.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_SendGamepadEffect(SDL_Gamepad *gamepad, const void *data, int size);
```

## Function Parameters

|                              |             |                                             |
| ---------------------------- | ----------- | ------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | The gamepad to affect                       |
| const void *                 | **data**    | The data to send to the gamepad             |
| int                          | **size**    | The size of the data to send to the gamepad |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

