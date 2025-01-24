# SDL_GUIDToString

Get an ASCII string representation for a given [SDL_GUID](SDL_GUID).

## Header File

Defined in [<SDL3/SDL_guid.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_guid.h)

## Syntax

```c
void SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);
```

## Function Parameters

|                      |             |                                                         |
| -------------------- | ----------- | ------------------------------------------------------- |
| [SDL_GUID](SDL_GUID) | **guid**    | the [SDL_GUID](SDL_GUID) you wish to convert to string. |
| char *               | **pszGUID** | buffer in which to write the ASCII string.              |
| int                  | **cbGUID**  | the size of pszGUID, should be at least 33 bytes.       |

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_StringToGUID](SDL_StringToGUID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGUID](CategoryGUID)

