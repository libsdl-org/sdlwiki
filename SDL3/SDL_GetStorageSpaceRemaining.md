###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetStorageSpaceRemaining

Queries the remaining space in a storage container.

## Header File

Defined in [SDL_storage.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_storage.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
Uint64 SDL_GetStorageSpaceRemaining(SDL_Storage *storage);

```

## Function Parameters

|                 |                              |
| --------------- | ---------------------------- |
| **storage**     | a storage container to query |

## Return Value

Returns the amount of remaining space, in bytes

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_StorageReady](SDL_StorageReady)
* [SDL_WriteStorageFile](SDL_WriteStorageFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

