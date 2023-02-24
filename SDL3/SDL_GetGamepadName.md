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

## Remarks

This is the same name as returned by
[SDL_GetGamepadNameForIndex](SDL_GetGamepadNameForIndex)(), but it takes a
gamepad identifier instead of the (unstable) device index.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadNameForIndex](SDL_GetGamepadNameForIndex)
* [SDL_OpenGamepad](SDL_OpenGamepad)

----
[CategoryAPI](CategoryAPI)

