###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StorageSpaceRemaining

Queries the remaining space in a storage container.

## Syntax

```c
Uint64 SDL_StorageSpaceRemaining(SDL_Storage *storage);

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
* [SDL_StorageFileSize](SDL_StorageFileSize)
* [SDL_StorageReadFile](SDL_StorageReadFile)
* [SDL_StorageReadFileAsync](SDL_StorageReadFileAsync)
* [SDL_StorageWriteFile](SDL_StorageWriteFile)
* [SDL_StorageWriteFileAsync](SDL_StorageWriteFileAsync)

----
[CategoryAPI](CategoryAPI)

