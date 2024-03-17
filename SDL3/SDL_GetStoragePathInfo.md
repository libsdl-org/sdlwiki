###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetStoragePathInfo

Get information about a filesystem path in a storage container.

## Syntax

```c
int SDL_GetStoragePathInfo(SDL_Storage *storage, const char *path, SDL_PathInfo *info);

```

## Function Parameters

|                 |                                                     |
| --------------- | --------------------------------------------------- |
| **storage**     | a storage container                                 |
| **path**        | the path to query                                   |
| **info**        | a pointer filled in with information about the path |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI)

