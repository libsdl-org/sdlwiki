###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_WriteStorageFile

Synchronously write a file from client memory into a storage container.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_WriteStorageFile(SDL_Storage *storage, const char *path, const void *source, Uint64 length);
```

## Function Parameters

|                              |             |                                         |
| ---------------------------- | ----------- | --------------------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage** | a storage container to write to.        |
| const char *                 | **path**    | the relative path of the file to write. |
| const void *                 | **source**  | a client-provided buffer to write from. |
| [Uint64](Uint64)             | **length**  | the length of the source buffer.        |

## Return Value

(bool) Returns true if the file was written or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the destination file size does not exactly match the size of the source buffer for any reason, this function will return false.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetStorageSpaceRemaining](SDL_GetStorageSpaceRemaining)
- [SDL_ReadStorageFile](SDL_ReadStorageFile)
- [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

