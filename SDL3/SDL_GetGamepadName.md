###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetGamepadName

Get the implementation-dependent name for an opened gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadName(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                                                                                   |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)(). |

## Return Value

(const char *) Returns the implementation dependent name for the gamepad,
or NULL if there is no name or the identifier passed is invalid.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetGamepadNameForID](SDL_GetGamepadNameForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

