###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GamepadConnected

Check if a gamepad has been opened and is currently connected.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
bool SDL_GamepadConnected(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                                                                                   |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)(). |

## Return Value

(bool) Returns true if the gamepad has been opened and is currently
connected, or false if not.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

