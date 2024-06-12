###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GUIDFromString

Convert a GUID string into a [SDL_GUID](SDL_GUID) structure.

## Header File

Defined in [<SDL3/SDL_guid.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_guid.h)

## Syntax

```c
SDL_GUID SDL_GUIDFromString(const char *pchGUID);
```

## Function Parameters

|              |             |                                                     |
| ------------ | ----------- | --------------------------------------------------- |
| const char * | **pchGUID** | string containing an ASCII representation of a GUID |

## Return Value

([SDL_GUID](SDL_GUID)) Returns a [SDL_GUID](SDL_GUID) structure.

## Remarks

Performs no error checking. If this function is given a string containing
an invalid GUID, the function will silently succeed, but the GUID generated
will not be useful.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GUIDToString](SDL_GUIDToString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGUID](CategoryGUID)

