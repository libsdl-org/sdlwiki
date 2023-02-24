###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetGUIDString

Get an ASCII string representation for a given [SDL_JoystickGUID](SDL_JoystickGUID).

## Syntax

```c
void SDL_JoystickGetGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **guid**        | the [SDL_JoystickGUID](SDL_JoystickGUID) you wish to convert to string |
| **pszGUID**     | buffer in which to write the ASCII string                              |
| **cbGUID**      | the size of pszGUID                                                    |

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetDeviceGUID](SDL_JoystickGetDeviceGUID)
* [SDL_JoystickGetGUID](SDL_JoystickGetGUID)
* [SDL_JoystickGetGUIDFromString](SDL_JoystickGetGUIDFromString)

----
[CategoryAPI](CategoryAPI)

