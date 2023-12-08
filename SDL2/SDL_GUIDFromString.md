###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GUIDFromString

Convert a GUID string into a ::[SDL_GUID](SDL_GUID.md) structure.

## Syntax

```c
SDL_GUID SDL_GUIDFromString(const char *pchGUID);

```

## Function Parameters

|                 |                                                     |
| --------------- | --------------------------------------------------- |
| **pchGUID**     | string containing an ASCII representation of a GUID |

## Return Value

Returns a ::[SDL_GUID](SDL_GUID.md) structure.

## Remarks

Performs no error checking. If this function is given a string containing
an invalid GUID, the function will silently succeed, but the GUID generated
will not be useful.

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_GUIDToString](SDL_GUIDToString.md)

----
[CategoryAPI](CategoryAPI.md)
