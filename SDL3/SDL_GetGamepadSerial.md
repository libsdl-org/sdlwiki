# SDL_GetGamepadSerial

Get the serial number of an opened gamepad, if available.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadSerial(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                              |
| ---------------------------- | ----------- | ---------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | the gamepad object to query. |

## Return Value

(const char *) Returns the serial number, or NULL if unavailable.

## Remarks

Returns the serial number of the gamepad, or NULL if it is not available.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

