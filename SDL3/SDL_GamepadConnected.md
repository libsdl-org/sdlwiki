###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadConnected

Check if a gamepad has been opened and is currently connected.

## Syntax

```c
SDL_bool SDL_GamepadConnected(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the gamepad has been opened and is
currently connected, or [SDL_FALSE](SDL_FALSE) if not.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CloseGamepad](SDL_CloseGamepad)
* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

