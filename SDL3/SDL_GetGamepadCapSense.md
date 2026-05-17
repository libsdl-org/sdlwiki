# SDL_GetGamepadCapSense

Get the current state of a capsense on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GetGamepadCapSense(SDL_Gamepad *gamepad, SDL_GamepadCapSenseType type);
```

## Function Parameters

|                                                    |             |                                |
| -------------------------------------------------- | ----------- | ------------------------------ |
| [SDL_Gamepad](SDL_Gamepad) *                       | **gamepad** | a gamepad.                     |
| [SDL_GamepadCapSenseType](SDL_GamepadCapSenseType) | **type**    | the type of capsense to query. |

## Return Value

(bool) Returns true if the capsense is touched, false otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_GamepadHasCapSense](SDL_GamepadHasCapSense)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

