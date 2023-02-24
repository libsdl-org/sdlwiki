###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadHasRumble

Query whether a gamepad has rumble support.

## Syntax

```c
SDL_bool SDL_GamepadHasRumble(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                      |
| --------------- | -------------------- |
| **gamepad**     | The gamepad to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE), or [SDL_FALSE](SDL_FALSE) if this gamepad
does not have rumble support

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_RumbleGamepad](SDL_RumbleGamepad)

----
[CategoryAPI](CategoryAPI)

