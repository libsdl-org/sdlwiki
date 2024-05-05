###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadProductVersion

Get the product version of an opened gamepad, if available.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
Uint16 SDL_GetGamepadProductVersion(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the USB product version, or zero if unavailable.

## Remarks

If the product version isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadInstanceProductVersion](SDL_GetGamepadInstanceProductVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

