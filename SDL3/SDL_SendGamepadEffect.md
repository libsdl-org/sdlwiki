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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

