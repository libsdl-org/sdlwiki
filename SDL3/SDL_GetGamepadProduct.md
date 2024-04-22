###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadProduct

Get the USB product ID of an opened gamepad, if available.

## Header File

Defined in [SDL_gamepad.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
Uint16 SDL_GetGamepadProduct(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the USB product ID, or zero if unavailable.

## Remarks

If the product ID isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetGamepadInstanceProduct](SDL_GetGamepadInstanceProduct)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

