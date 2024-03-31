###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RemoveStoragePath

Remove a file or an empty directory in a writable storage container.

## Header File

Defined in [SDL_storage.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_RemoveStoragePath(SDL_Storage *storage, const char *path);

```

## Function Parameters

|                 |                                        |
| --------------- | -------------------------------------- |
| **storage**     | a storage container                    |
| **path**        | the path of the directory to enumerate |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_StorageReady](SDL_StorageReady)

----
[CategoryAPI](CategoryAPI)

