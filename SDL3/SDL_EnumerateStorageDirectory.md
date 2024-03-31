###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnumerateStorageDirectory

Enumerate a directory in a storage container.

## Header File

Defined in [SDL_storage.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_EnumerateStorageDirectory(SDL_Storage *storage, const char *path, SDL_EnumerateDirectoryCallback callback, void *userdata);

```

## Function Parameters

|                  |                                                           |
| ---------------- | --------------------------------------------------------- |
| **storage**      | a storage container                                       |
| **path**         | the path of the directory to enumerate                    |
| **callback**     | a function that is called for each entry in the directory |
| **userdata**     | a pointer that is passed to `callback`                    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI)

