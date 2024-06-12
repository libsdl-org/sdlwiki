###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GUIDToString

Get an ASCII string representation for a given [SDL_GUID](SDL_GUID).

## Header File

Defined in [<SDL3/SDL_guid.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_guid.h)

## Syntax

```c
int SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);
```

## Function Parameters

|                      |             |                                                        |
| -------------------- | ----------- | ------------------------------------------------------ |
| [SDL_GUID](SDL_GUID) | **guid**    | the [SDL_GUID](SDL_GUID) you wish to convert to string |
| char *               | **pszGUID** | buffer in which to write the ASCII string              |
| int                  | **cbGUID**  | the size of pszGUID                                    |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GUIDFromString](SDL_GUIDFromString)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGUID](CategoryGUID)

