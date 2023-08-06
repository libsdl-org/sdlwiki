###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadName

Get the implementation-dependent name for an opened gamepad.

## Syntax

```c
const char* SDL_GetGamepadName(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **gamepad**     | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)() |

## Return Value

Returns the implementation dependent name for the gamepad, or NULL if there
is no name or the identifier passed is invalid.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadInstanceName](SDL_GetGamepadInstanceName)
* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

