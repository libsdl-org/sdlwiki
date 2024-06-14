###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteStorageFile

Synchronously write a file from client memory into a storage container.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
int SDL_WriteStorageFile(SDL_Storage *storage, const char *path, const void *source, Uint64 length);
```

## Function Parameters

|                              |             |                                         |
| ---------------------------- | ----------- | --------------------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage** | a storage container to write to.        |
| const char *                 | **path**    | the relative path of the file to write. |
| const void *                 | **source**  | a client-provided buffer to write from. |
| Uint64                       | **length**  | the length of the source buffer.        |

## Return Value

(int) Returns 0 if the file was written, a negative value otherwise; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetStorageSpaceRemaining](SDL_GetStorageSpaceRemaining)
- [SDL_ReadStorageFile](SDL_ReadStorageFile)
- [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

