###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetStorageSpaceRemaining

Queries the remaining space in a storage container.

## Syntax

```c
Uint64 SDL_GetStorageSpaceRemaining(SDL_Storage *storage);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **storage**     | a storage container to query |

## Return Value

Returns the amount of remaining space, in bytes

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenTitleStorage](SDL_OpenTitleStorage)
* [SDL_OpenUserStorage](SDL_OpenUserStorage)
* [SDL_OpenStorage](SDL_OpenStorage)
* [SDL_CloseStorage](SDL_CloseStorage)
* [SDL_StorageReady](SDL_StorageReady)
* [SDL_GetStorageFileSize](SDL_GetStorageFileSize)
* [SDL_ReadStorageFile](SDL_ReadStorageFile)
* [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI)

