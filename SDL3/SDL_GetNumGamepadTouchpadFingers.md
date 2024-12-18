###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetGamepadTouchpadFinger](SDL_GetGamepadTouchpadFinger)
- [SDL_GetNumGamepadTouchpads](SDL_GetNumGamepadTouchpads)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

