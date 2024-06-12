###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadMappingForGUID

Get the gamepad mapping string for a given GUID.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
char * SDL_GetGamepadMappingForGUID(SDL_JoystickGUID guid);
```

## Function Parameters

|                                      |          |                                                                |
| ------------------------------------ | -------- | -------------------------------------------------------------- |
| [SDL_JoystickGUID](SDL_JoystickGUID) | **guid** | a structure containing the GUID for which a mapping is desired |

## Return Value

(char *) Returns a mapping string or NULL on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The returned string must be freed with [SDL_free](SDL_free)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickInstanceGUID](SDL_GetJoystickInstanceGUID)
- [SDL_GetJoystickGUID](SDL_GetJoystickGUID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

