###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadHasLED

Query whether a gamepad has an LED.

## Syntax

```c
SDL_bool SDL_GamepadHasLED(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                      |
| --------------- | -------------------- |
| **gamepad**     | The gamepad to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE), or [SDL_FALSE](SDL_FALSE) if this gamepad
does not have a modifiable LED

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

