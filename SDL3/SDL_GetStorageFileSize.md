###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetStorageFileSize

Query the size of a file within a storage container.

## Header File

Defined in [SDL_storage.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
int SDL_GetStorageFileSize(SDL_Storage *storage, const char *path, Uint64 *length);

```

## Function Parameters

|                 |                                               |
| --------------- | --------------------------------------------- |
| **storage**     | a storage container to query                  |
| **path**        | the relative path of the file to query        |
| **length**      | a pointer to be filled with the file's length |

## Return Value

Returns 0 if the file could be queried, a negative value otherwise; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_ReadStorageFile](SDL_ReadStorageFile)
* [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

