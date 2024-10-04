###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetStoragePathInfo

Get information about a filesystem path in a storage container.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_GetStoragePathInfo(SDL_Storage *storage, const char *path, SDL_PathInfo *info);
```

## Function Parameters

|                                |             |                                                                                                    |
| ------------------------------ | ----------- | -------------------------------------------------------------------------------------------------- |
| [SDL_Storage](SDL_Storage) *   | **storage** | a storage container.                                                                               |
| const char *                   | **path**    | the path to query.                                                                                 |
| [SDL_PathInfo](SDL_PathInfo) * | **info**    | a pointer filled in with information about the path, or NULL to check for the existence of a file. |

## Return Value

(bool) Returns true on success or false if the file doesn't exist, or
another failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

