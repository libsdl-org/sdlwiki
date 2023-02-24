###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadVendor

Get the USB vendor ID of an opened gamepad, if available.

## Syntax

```c
Uint16 SDL_GetGamepadVendor(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the USB vendor ID, or zero if unavailable.

## Remarks

If the vendor ID isn't available this function returns 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

