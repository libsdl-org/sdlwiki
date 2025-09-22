# SDL_GetGamepadPath

Get the implementation-dependent path for an opened gamepad.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadPath(SDL_Gamepad *gamepad);
```

## Function Parameters

|                              |             |                                                                                   |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------- |
| [SDL_Gamepad](SDL_Gamepad) * | **gamepad** | a gamepad identifier previously returned by [SDL_OpenGamepad](SDL_OpenGamepad)(). |

## Return Value

(const char *) Returns the implementation dependent path for the gamepad,
or NULL if there is no path or the identifier passed is invalid.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadPathForID](SDL_GetGamepadPathForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

