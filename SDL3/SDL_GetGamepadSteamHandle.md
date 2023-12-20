###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadSteamHandle

Get the Steam Input handle of an opened gamepad, if available.

## Syntax

```c
Uint64 SDL_GetGamepadSteamHandle(SDL_Gamepad *gamepad);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **gamepad**     | the gamepad object to query. |

## Return Value

Returns the gamepad handle, or 0 if unavailable.

## Remarks

Returns an InputHandle_t for the gamepad that can be used with Steam Input
API: https://partner.steamgames.com/doc/api/ISteamInput

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

