###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StorageReadFile

Synchronously read a file from a storage container into a client-provided buffer.

## Syntax

```c
int SDL_StorageReadFile(SDL_Storage *storage, const char *path, void *destination, Uint64 length);

```

## Function Parameters

|                     |                                                |
| ------------------- | ---------------------------------------------- |
| **storage**         | a storage container to read from               |
| **path**            | the relative path of the file to read          |
| **destination**     | a client-provided buffer to read the file into |
| **length**          | the length of the destination buffer           |

## Return Value

Returns 0 if the file was read, a negative value otherwise; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenTitleStorage](SDL_OpenTitleStorage)
* [SDL_OpenUserStorage](SDL_OpenUserStorage)
* [SDL_OpenStorage](SDL_OpenStorage)
* [SDL_CloseStorage](SDL_CloseStorage)
* [SDL_StorageReady](SDL_StorageReady)
* [SDL_StorageFileSize](SDL_StorageFileSize)
* [SDL_StorageWriteFile](SDL_StorageWriteFile)
* [SDL_StorageSpaceRemaining](SDL_StorageSpaceRemaining)

----
[CategoryAPI](CategoryAPI)

