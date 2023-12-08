###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerMappingForGUID

Get the game controller mapping string for a given GUID.

## Syntax

```c
char * SDL_GameControllerMappingForGUID(SDL_JoystickGUID guid);

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

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetDeviceGUID](SDL_JoystickGetDeviceGUID.md)
* [SDL_JoystickGetGUID](SDL_JoystickGetGUID.md)

----
[CategoryAPI](CategoryAPI.md)
