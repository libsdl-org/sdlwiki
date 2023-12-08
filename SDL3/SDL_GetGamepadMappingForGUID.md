###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadMappingForGUID

Get the gamepad mapping string for a given GUID.

## Syntax

```c
char * SDL_GetGamepadMappingForGUID(SDL_JoystickGUID guid);

```

## Function Parameters

|              |                                                                |
| ------------ | -------------------------------------------------------------- |
| **guid**     | a structure containing the GUID for which a mapping is desired |

## Return Value

Returns a mapping string or NULL on error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The returned string must be freed with [SDL_free](SDL_free.md)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickInstanceGUID](SDL_GetJoystickInstanceGUID.md)
* [SDL_GetJoystickGUID](SDL_GetJoystickGUID.md)

----
[CategoryAPI](CategoryAPI.md)
