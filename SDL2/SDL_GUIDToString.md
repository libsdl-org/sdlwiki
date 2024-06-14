###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GUIDToString

Get an ASCII string representation for a given [SDL_GUID](SDL_GUID).

## Header File

Defined in [SDL_guid.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_guid.h)

## Syntax

```c
void SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);
```

## Function Parameters

|                      |             |                                                         |
| -------------------- | ----------- | ------------------------------------------------------- |
| [SDL_GUID](SDL_GUID) | **guid**    | the [SDL_GUID](SDL_GUID) you wish to convert to string. |
| char *               | **pszGUID** | buffer in which to write the ASCII string.              |
| int                  | **cbGUID**  | the size of pszGUID.                                    |

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GUIDFromString](SDL_GUIDFromString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGUID](CategoryGUID)

