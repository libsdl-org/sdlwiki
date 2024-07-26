###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadMappingForGUID

Get the gamepad mapping string for a given GUID.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadMappingForGUID(SDL_GUID guid);
```

## Function Parameters

|                      |          |                                                                 |
| -------------------- | -------- | --------------------------------------------------------------- |
| [SDL_GUID](SDL_GUID) | **guid** | a structure containing the GUID for which a mapping is desired. |

## Return Value

(const char *) Returns a mapping string or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetJoystickGUIDForID](SDL_GetJoystickGUIDForID)
- [SDL_GetJoystickGUID](SDL_GetJoystickGUID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

