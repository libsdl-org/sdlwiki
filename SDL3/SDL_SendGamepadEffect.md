# SDL_SendGamepadEffect

Send a gamepad specific effect packet.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_SendGamepadEffect(SDL_Gamepad *gamepad, const void *data, int size);
```

## Function Parameters

|                              |             |                                              |
| ---------------------------- | ----------- | -------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | the gamepad to affect.                       |
| const void *                 | **data**    | the data to send to the gamepad.             |
| int                          | **size**    | the size of the data to send to the gamepad. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

