# SDL_GetNumGamepadTouchpadFingers

Get the number of supported simultaneous fingers on a touchpad on a game gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_GetNumGamepadTouchpadFingers(SDL_Gamepad *gamepad, int touchpad);
```

## Function Parameters

|                              |              |             |
| ---------------------------- | ------------ | ----------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad**  | a gamepad.  |
| int                          | **touchpad** | a touchpad. |

## Return Value

(int) Returns number of supported simultaneous fingers.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadTouchpadFinger](SDL_GetGamepadTouchpadFinger)
- [SDL_GetNumGamepadTouchpads](SDL_GetNumGamepadTouchpads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

