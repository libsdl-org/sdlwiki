###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetStorageSpaceRemaining

Queries the remaining space in a storage container.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
Uint64 SDL_GetStorageSpaceRemaining(SDL_Storage *storage);
```

## Function Parameters

|                              |             |                               |
| ---------------------------- | ----------- | ----------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage** | a storage container to query. |

## Return Value

([Uint64](Uint64)) Returns the amount of remaining space, in bytes.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_StorageReady](SDL_StorageReady)
- [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

