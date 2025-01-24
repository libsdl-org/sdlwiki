# SDL_GetGamepadMappingForGUID

Get the gamepad mapping string for a given GUID.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
char * SDL_GetGamepadMappingForGUID(SDL_GUID guid);
```

## Function Parameters

|                      |          |                                                                 |
| -------------------- | -------- | --------------------------------------------------------------- |
| [SDL_GUID](SDL_GUID) | **guid** | a structure containing the GUID for which a mapping is desired. |

## Return Value

(char *) Returns a mapping string or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickGUIDForID](SDL_GetJoystickGUIDForID)
- [SDL_GetJoystickGUID](SDL_GetJoystickGUID)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

