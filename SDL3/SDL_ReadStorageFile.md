###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadStorageFile

Synchronously read a file from a storage container into a client-provided buffer.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
int SDL_ReadStorageFile(SDL_Storage *storage, const char *path, void *destination, Uint64 length);
```

## Function Parameters

|                              |                 |                                                 |
| ---------------------------- | --------------- | ----------------------------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage**     | a storage container to read from.               |
| const char *                 | **path**        | the relative path of the file to read.          |
| void *                       | **destination** | a client-provided buffer to read the file into. |
| Uint64                       | **length**      | the length of the destination buffer.           |

## Return Value

(int) Returns 0 if the file was read, a negative value otherwise; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetStorageFileSize](SDL_GetStorageFileSize)
- [SDL_StorageReady](SDL_StorageReady)
- [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

