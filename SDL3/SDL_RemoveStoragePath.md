###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RemoveStoragePath

Remove a file or an empty directory in a writable storage container.

## Header File

Defined in [<SDL3/SDL_storage.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h)

## Syntax

```c
bool SDL_RemoveStoragePath(SDL_Storage *storage, const char *path);
```

## Function Parameters

|                              |             |                                         |
| ---------------------------- | ----------- | --------------------------------------- |
| [SDL_Storage](SDL_Storage) * | **storage** | a storage container.                    |
| const char *                 | **path**    | the path of the directory to enumerate. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStorage](CategoryStorage)

