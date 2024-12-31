###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ReadStorageFile

Synchronously read a file from a storage container into a client-provided buffer.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_ReadStorageFile(SDL_Storage *storage, const char *path, void *destination, Uint64 length);
```

## Function Parameters

|                              |                 |                                                 |
| ---------------------------- | --------------- | ----------------------------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage**     | a storage container to read from.               |
| const char *                 | **path**        | the relative path of the file to read.          |
| void *                       | **destination** | a client-provided buffer to read the file into. |
| [Uint64](Uint64)             | **length**      | the length of the destination buffer.           |

## Return Value

(bool) Returns true if the file was read or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The value of `length` must match the length of the file exactly; call [SDL_GetStorageFileSize](SDL_GetStorageFileSize)() to get this value. This behavior may be relaxed in a future release.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetStorageFileSize](SDL_GetStorageFileSize)
- [SDL_StorageReady](SDL_StorageReady)
- [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

