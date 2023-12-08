###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GUIDToString

Get an ASCII string representation for a given ::[SDL_GUID](SDL_GUID.md).

## Syntax

```c
void SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **guid**        | the ::[SDL_GUID](SDL_GUID.md) you wish to convert to string |
| **pszGUID**     | buffer in which to write the ASCII string                |
| **cbGUID**      | the size of pszGUID                                      |

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_GUIDFromString](SDL_GUIDFromString.md)

----
[CategoryAPI](CategoryAPI.md)
