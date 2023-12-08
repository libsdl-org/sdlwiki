###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickGetGUIDFromString

Convert a GUID string into a [SDL_JoystickGUID](SDL_JoystickGUID.md) structure.

## Syntax

```c
SDL_JoystickGUID SDL_JoystickGetGUIDFromString(const char *pchGUID);

```

## Function Parameters

|                 |                                                     |
| --------------- | --------------------------------------------------- |
| **pchGUID**     | string containing an ASCII representation of a GUID |

## Return Value

Returns a [SDL_JoystickGUID](SDL_JoystickGUID.md) structure.

## Remarks

Performs no error checking. If this function is given a string containing
an invalid GUID, the function will silently succeed, but the GUID generated
will not be useful.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickGetGUIDString](SDL_JoystickGetGUIDString.md)

----
[CategoryAPI](CategoryAPI.md)
