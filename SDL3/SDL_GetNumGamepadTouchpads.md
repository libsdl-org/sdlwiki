# SDL_GetNumGamepadTouchpads

Get the number of touchpads on a gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_GetNumGamepadTouchpads(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |            |
| ---------------------------- | ----------- | ---------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad. |

## Return Value

(int) Returns number of touchpads.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumGamepadTouchpadFingers](SDL_GetNumGamepadTouchpadFingers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

