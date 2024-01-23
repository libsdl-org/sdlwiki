###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadCaps

Query gamepad capabilities 

## Syntax

```c
Uint32 SDL_GetGamepadCaps(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                      |
| --------------- | -------------------- |
| **gamepad**     | The gamepad to query |

## Return Value

Returns a mask of [SDL_GamepadCaps](SDL_GamepadCaps) values indicating the
gamepad capabilities.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

