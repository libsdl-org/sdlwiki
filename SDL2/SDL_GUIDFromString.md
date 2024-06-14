###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GUIDFromString

Convert a GUID string into a [SDL_GUID](SDL_GUID) structure.

## Header File

Defined in [SDL_guid.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_guid.h)

## Syntax

```c
SDL_GUID SDL_GUIDFromString(const char *pchGUID);
```

## Function Parameters

|              |             |                                                      |
| ------------ | ----------- | ---------------------------------------------------- |
| const char * | **pchGUID** | string containing an ASCII representation of a GUID. |

## Return Value

([SDL_GUID](SDL_GUID)) Returns a [SDL_GUID](SDL_GUID) structure.

## Remarks

Performs no error checking. If this function is given a string containing
an invalid GUID, the function will silently succeed, but the GUID generated
will not be useful.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GUIDToString](SDL_GUIDToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGUID](CategoryGUID)

