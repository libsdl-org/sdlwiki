###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenStorage

Opens up a container using a client-provided storage interface.

## Header File

Defined in [SDL_storage.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_Storage* SDL_OpenStorage(const SDL_StorageInterface *iface, void *userdata);

```

## Function Parameters

|                  |                                                        |
| ---------------- | ------------------------------------------------------ |
| **iface**        | the function table to be used by this container        |
| **userdata**     | the pointer that will be passed to the store interface |

## Return Value

Returns a storage container on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_Storage](SDL_Storage) implementation. If you just need an
[SDL_Storage](SDL_Storage), you should use the built-in implementations in
SDL, like [SDL_OpenTitleStorage](SDL_OpenTitleStorage)() or
[SDL_OpenUserStorage](SDL_OpenUserStorage)().

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_CloseStorage](SDL_CloseStorage)
* [SDL_GetStorageFileSize](SDL_GetStorageFileSize)
* [SDL_GetStorageSpaceRemaining](SDL_GetStorageSpaceRemaining)
* [SDL_ReadStorageFile](SDL_ReadStorageFile)
* [SDL_StorageReady](SDL_StorageReady)
* [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

