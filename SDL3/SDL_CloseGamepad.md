###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseGamepad

Close a gamepad previously opened with [SDL_OpenGamepad](SDL_OpenGamepad)().

## Syntax

```c
void SDL_CloseGamepad(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

