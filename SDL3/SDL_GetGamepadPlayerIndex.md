###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadPlayerIndex

Get the player index of an opened gamepad.

## Syntax

```c
int SDL_GetGamepadPlayerIndex(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the player index for gamepad, or -1 if it's not available.

## Remarks

For XInput gamepads this returns the XInput user index.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

