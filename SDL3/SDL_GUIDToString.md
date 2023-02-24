###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GUIDToString

Get an ASCII string representation for a given ::[SDL_GUID](SDL_GUID).

## Syntax

```c
int SDL_GUIDToString(SDL_GUID guid, char *pszGUID, int cbGUID);

```

## Function Parameters

|                 |                                                          |
| --------------- | -------------------------------------------------------- |
| **guid**        | the ::[SDL_GUID](SDL_GUID) you wish to convert to string |
| **pszGUID**     | buffer in which to write the ASCII string                |
| **cbGUID**      | the size of pszGUID                                      |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GUIDFromString](SDL_GUIDFromString)

----
[CategoryAPI](CategoryAPI)

